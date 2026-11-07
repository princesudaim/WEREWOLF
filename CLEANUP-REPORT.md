# Cleanup report

No current sound, current selectable avatar, role marker, role art, skin, background or font was removed. All71WAVs and19selectable avatars, including your7original supplied photos, are kept byte-for-byte. Gameplay, both Muter repeat settings, use limits, role history, scoring and recovery are unchanged.

## Removed from code/assets (27physical files)

18unused starter source files belonged to a second, unreachable game. The4old crew photos were used only by that starter, not the current19-avatar picker. Each also had an ignored local Source/public copy. One Python bytecode cache was generated junk.

- `Werewolf-Game/Source/src/App.tsx` — 9424bytes
- `Werewolf-Game/Source/src/components/Avatar.tsx` — 9202bytes
- `Werewolf-Game/Source/src/components/DayScreen.tsx` — 10969bytes
- `Werewolf-Game/Source/src/components/GameOverScreen.tsx` — 8425bytes
- `Werewolf-Game/Source/src/components/LobbyScreen.tsx` — 15367bytes
- `Werewolf-Game/Source/src/components/NightScreen.tsx` — 20152bytes
- `Werewolf-Game/Source/src/components/RevealScreen.tsx` — 6547bytes
- `Werewolf-Game/Source/src/components/SettingsScreen.tsx` — 12508bytes
- `Werewolf-Game/Source/src/components/StartScreen.tsx` — 8337bytes
- `Werewolf-Game/Source/src/components/ui.tsx` — 20510bytes
- `Werewolf-Game/Source/src/index.css` — 5776bytes
- `Werewolf-Game/Source/src/lib/audio.ts` — 1621bytes
- `Werewolf-Game/Source/src/lib/avatars.ts` — 3579bytes
- `Werewolf-Game/Source/src/lib/engine.ts` — 13941bytes
- `Werewolf-Game/Source/src/lib/fx.ts` — 6374bytes
- `Werewolf-Game/Source/src/lib/storage.ts` — 1626bytes
- `Werewolf-Game/Source/src/lib/types.ts` — 3121bytes
- `Werewolf-Game/Source/src/utils/cn.ts` — 169bytes
- `Werewolf-Game/Source/public/avatars/crew-12.jpg` — 5152bytes
- `Werewolf-Game/Source/public/avatars/crew-13.jpg` — 6353bytes
- `Werewolf-Game/Source/public/avatars/crew-14.jpg` — 2784bytes
- `Werewolf-Game/Source/public/avatars/crew-15.png` — 1771454bytes
- `Werewolf-Game/Website/avatars/crew-12.jpg` — 5152bytes
- `Werewolf-Game/Website/avatars/crew-13.jpg` — 6353bytes
- `Werewolf-Game/Website/avatars/crew-14.jpg` — 2784bytes
- `Werewolf-Game/Website/avatars/crew-15.png` — 1771454bytes
- `Werewolf-Game/Source/scripts/__pycache__/prepare-card-reveals.cpython-311.pyc` — 16025bytes

## Removed unused direct dependencies

- `clsx`
- `tailwind-merge`
- `tailwindcss`
- `@tailwindcss/vite`

The lockfile no longer contains 22 package entries required only by the removed tooling. Exact entry names and before-file hashes are in CLEANUP-REPORT.json.

## Removed obsolete download/build code

- The unused development-only ZIP route and its Vite plugin. There is still no in-game Download Game button.
- The old default ZIP format with duplicate Website + Source/public media. The default ZIP now contains just the root-ready game, this report, guide and checker.

## Excluded from the launch ZIP, not deleted from your project

Editable current source, tests, audio preparation scripts, dependency folders, Git metadata, local QA/screenshots/caches, environment files, private browser data and older backups. The editable project remains in the repository.

## Old saves

No Drive backup was deleted or replaced. The named finaleee last version archive is preserved.
