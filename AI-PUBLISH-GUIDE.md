# READ FIRST — publish this Werewolf game, with ALL sounds and avatars

Release: `ccb7605348df`. This ZIP is the finished game, not a source project.
No npm install/build, API, database, secrets or external media service is required
for publishing these extracted files. Do not make replacement photos or sounds.

## The shortest correct procedure

1. Download the ZIP from its shared Drive/file link. Extract it completely.
2. In that extracted folder, run `python3 VERIFY-LAUNCH.py` (Windows: `py VERIFY-LAUNCH.py`).
   It must PASS. The folder must contain index.html, sw.js, werewolf/, icons/,
   manifest.webmanifest, RELEASE.json and .nojekyll at the SAME level.
3. Publish that ENTIRE extracted folder to the approved host's public root,
   keeping exact filenames, letter case, bytes and directories. Do not publish
   only index.html, the ZIP itself, or an extra outer ZIP-name folder.
4. Open the actual published project URL. Then verify ALL published bytes:

   `python3 VERIFY-LAUNCH.py --url https://OWNER.github.io/REPOSITORY/`

   Substitute the actual URL. Do not invent a success URL. This command reads the
   local release manifest and checks that the host serves that exact release.
5. Test the avatar picker and sound previews, not just the home screen.
   First visit online; allow offline setup to finish. At the menu, close all game
   tabs/app windows and reopen before testing offline use or accepting an update.

## Publishing to GitHub Pages

- Use the repository/branch the owner approves. In an Arena checkout, keep the
  existing session branch: never rename it, switch branches or create a new one.
- Prefer uploading the whole extracted tree with git. Text-only AI editing,
  copying HTML, or pasting binary data into chat does NOT transfer images/WAVs.
  Browser upload tools can impose file-count and size limits; check their result.
- With the owner's approval, copy files without deleting unrelated repository
  content, inspect `git status --short`, then add/commit/push the intended files.
  If media is excluded, inspect `git check-ignore -v PATH`, not just HTML changes.
- For branch-based Pages: Settings → Pages → Deploy from a branch → the approved
  branch → /(root). If publishing a source repository's Werewolf-Game/Website
  layout instead, retain its root launcher and WHOLE Website folder.
- If there is an existing Pages Actions workflow, inspect it first. Use one
  publisher and make its artifact the entire built site, not src/ or index.html.
  Do not add a competing workflow or assume branch Pages and Actions are the same.
- Keep .nojekyll. Do not rewrite media bytes, minify index.html again, recompress
  WAVs, rename directories or replace the worker separately: exact-build offline
  checksums must stay consistent. No Git LFS pointers, HTML error pages, Drive
  preview pages or API metadata should be uploaded in place of real binary files.
- Ask for authorization before committing/pushing/deploying. For authentication
  errors, reconnect GitHub through the platform; never ask for account passwords,
  personal access tokens, OAuth tokens or 2FA codes in chat.

## Why images/sounds may be missing

These are diagnosed project/publishing traps, NOT a claimed reconstruction of
another AI's error log (that log and its live site were not supplied):

1. **Only HTML copied.** The JS/CSS and small marker art are bundled in index.html,
   but 71 real WAVs, current photos, role art, backgrounds and fonts are separate
   relative files. Copy the entire werewolf/ tree and the other runtime files.
   Catalog `file` values are the playable WAV URLs. A `source` field naming an
   original MP3 is provenance, not an extra file to find/upload or rename.
2. **Wrong app edited.** An unused starter App/components/lib implementation used
   different avatars and synthetic audio. It was removed. The ONLY current entry
   is src/main.tsx → src/Werewolf.tsx. Current selectable photos are defined in
   src/avatar-assignment.ts; sound catalogs/controllers are directly under src/.
3. **Source/public missing after cloning.** Large source media is deliberately
   stored once in Werewolf-Game/Website; Source/public media copies are gitignored.
   Source build/dev now automatically restore missing originals from the shared
   manifest and fail clearly for missing required files. Do not build a source-only
   copy without its media. Do not remove the shared Website assets/manifest.
4. **Wrong/old branch or old cached release.** Workspace/Drive changes are not
   automatically pushed to GitHub. Compare RELEASE.json, HTML data-game-build and
   the actual publishing branch/artifact. Do not substitute an older source copy.
5. **Wrong folder/absolute paths/fallbacks.** A project URL includes /REPOSITORY/.
   Keep relative URLs. A WAV/image URL must return the binary file, not a 404,
   login page, redirect or index.html fallback. The checker identifies this.
6. **Autoplay/mute, not missing files.** Browsers may require an actual tap to
   start sound. Check device/site volume, Settings sound switches and individual
   volumes; use sound PREVIEW/RETRY controls. A 200 response alone is not proof of
   playback. Audio decoding and controller tests are not speaker certification.
7. **Offline installation rejects redirects/mixed files.** The worker checks
   exact SHA-256/size and rejects redirects when caching. Use ordinary static
   hosting; do not redirect canonical root/index or rewrite files during caching.
   The development preview now distinguishes navigation redirects from internal
   asset fetches. Never force-activate a worker or clear storage during a match.

## “Already downloaded”, but no ZIP in Downloads

Offline cache files live INSIDE the browser. They are not a portable ZIP and do
not appear in the device's Downloads folder. “Update downloaded” likewise means
a waiting browser-cache update. It does NOT mean this ZIP was downloaded.

Use the separate Drive/file link and its DOWNLOAD action to obtain this archive.
This game intentionally has no Download Game button. DOWNLOAD MISSING FILES is
only a missing-cache-file repair, not an archive downloader; when all cache files
are present, there is nothing to repair. Do not erase profiles, rankings, recovery
or browser storage to try to obtain a ZIP. A new host/origin has separate local data.

## Confirm the actual added media

- All 71 current WAV files are included unchanged. There is no looping music or
  animal ambience; recordings remain one-shot with their existing settings.
- All 19 selectable avatars are included. The 7 supplied ORIGINAL photos remain
  in displayed positions 1,2,3,5,6,7,8. See RELEASE.json for exact paths/hashes.
  They were not resized, cropped, regenerated or re-encoded during cleanup.
- Camera/gallery pictures selected inside a user's browser are private local
  profile data, not automatically publishable files. The supplied built-in photos
  above ARE part of this ZIP. Do not export a user's browser profile as an asset.
- The original Werewolf claw remains 90%, other active markers 48%. Current Muter
  settings, role history, gameplay, results/scoring and recovery are preserved.

## Test locally or edit source

To test this extracted launch folder, run `python3 -m http.server 8000` there and
open http://localhost:8000 on that same computer. This is local testing only,
not a public deployment. Opening index.html directly can run the game, but full
browser offline caching/recovery require supported HTTPS/localhost APIs.

To EDIT, use the separate editable repository, not this finished launch ZIP:

    cd Werewolf-Game/Source
    npm ci
    npx tsc --noEmit
    npm run test:unit
    npm run build

`npm run build` restores missing shared media automatically and now produces
ONE root-ready `dist/Werewolf-Game.zip`, with this guide and checker. It no longer
mixes a duplicate editable Source/public tree into the default archive.
For newly added files, keep their catalogs/relative URLs and public/sw.js CORE
list consistent; the build must verify every listed file and the unchanged64MiB
offline budget. Do not raise that budget or discard originals to hide a failure.

## If it still fails

Give the owner the exact failed command, full error text, publishing branch,
Pages workflow/artifact path, live URL, HTML build ID and one failing media URL
with status/Content-Type. Run the included checker and report its actual output.
Do not say “published” merely because a commit/HTML upload succeeded. Don't blame
all sounds or delete media without checking the exact file failure.

Read CLEANUP-REPORT.md for every deletion and CLEANUP-REPORT.json for hashes.
Existing Drive backups, especially “finaleee last version”, were not overwritten.
