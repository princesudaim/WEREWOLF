#!/usr/bin/env python3
"""Verify the extracted launch files or compare a published site to this release.
Python 3 standard library only. Read-only: never deletes files/browser data.
"""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import sys
from urllib.parse import quote, urljoin, urlsplit
from urllib.request import Request, urlopen


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--directory', type=Path, default=Path(__file__).resolve().parent,
                        help='Extracted folder containing RELEASE.json and index.html')
    parser.add_argument('--url', help='Optional actual published project URL, including its subdirectory')
    parser.add_argument('--timeout', type=float, default=15)
    args = parser.parse_args()
    root = args.directory.resolve()
    try:
        release = json.loads((root / 'RELEASE.json').read_text())
        expected = release['website_files']
        if not isinstance(expected, dict) or not expected or 'index.html' not in expected:
            raise ValueError('runtime manifest missing')
    except Exception as exc:
        print(f'FAIL: extract the complete launch ZIP first; cannot read {root / "RELEASE.json"}: {exc}', file=sys.stderr)
        return 1
    base = args.url
    if base:
        if urlsplit(base).scheme not in ('http', 'https') or urlsplit(base).query or urlsplit(base).fragment:
            print('FAIL: --url must be the HTTP(S) project folder URL, without query/fragment.', file=sys.stderr)
            return 1
        base = base.removesuffix('index.html').rstrip('/') + '/'
    failures = []
    checked = 0
    for name, item in sorted(expected.items()):
        try:
            parts = PurePosixPath(name)
            if parts.is_absolute() or '..' in parts.parts or '\\' in name:
                raise ValueError('unsafe manifest path')
            if base:
                url = urljoin(base, quote(name, safe='/'))
                with urlopen(Request(url, headers={'Cache-Control': 'no-cache'}), timeout=args.timeout) as response:
                    if response.geturl() != url:
                        raise ValueError(f'redirected to {response.geturl()} (publish canonical files, not preview redirects)')
                    data = response.read(item['size'] + 1)
                    if name.lower().endswith(('.wav', '.mp3', '.png', '.jpg', '.webp')) and 'text/html' in response.headers.get('Content-Type', ''):
                        raise ValueError('server returned an HTML error/fallback page instead of media')
            else:
                path = root / name
                if path.is_symlink():
                    raise ValueError('unexpected symlink; extract real files')
                data = path.read_bytes()
            if len(data) != item['size'] or hashlib.sha256(data).hexdigest() != item['sha256']:
                raise ValueError('size/SHA-256 mismatch: missing, changed, truncated or wrong-version file')
            checked += 1
        except Exception as exc:
            failures.append(name)
            print(f'FAIL {name}: {exc}', file=sys.stderr)
            if base and len(failures) >= 5:
                print('Stopped after 5 published-file errors; remaining files were NOT verified.', file=sys.stderr)
                break
    if failures:
        print(f'FAILED: {len(failures)} errors; {checked}/{len(expected)} runtime files verified. Upload the complete extracted ZIP unchanged.', file=sys.stderr)
        return 1
    counts = release.get('media', {})
    print(f'PASS release {release["revision"]}: {checked}/{len(expected)} runtime files match exactly; '
          f'{counts.get("wav_files", "?")} sound files, {len(counts.get("selectable_avatars", []))} selectable avatars. '
          + ('Published bytes verified.' if base else 'Extracted files verified.'))
    print('This proves file presence/integrity, not physical speaker output or browser autoplay permission.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
