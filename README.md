# Tekken Tag Tournament 2 — Community Windows Update

**v0.1.7-community.4 · 2026-10-29 · Prerelease**

An unofficial update for an existing USA/Europe TU3 installation of the
[native PC port](https://github.com/shihabal3amri/tekken-tag-tournament-2-pc).

## Download

[**Download the Windows updater**](https://github.com/ak1458/tekken-tag-tournament-2-pc/releases/download/v0.1.7-community.4/TTT2-Game-Update-v0.1.7-community.4.exe)
· [Checksums](https://github.com/ak1458/tekken-tag-tournament-2-pc/releases/download/v0.1.7-community.4/SHA256SUMS.txt)
· [Release notes](https://github.com/ak1458/tekken-tag-tournament-2-pc/releases/tag/v0.1.7-community.4)

## Install the update

1. Open the updater and click **Next**.
2. Browse to your existing game folder, then choose **Install → Finish**.
3. Open your usual game shortcut. Choose **Play Offline** (updated game) or
   **Play Online** (preserved original).

Existing game assets stay in place. Saves and settings remain in
`%LOCALAPPDATA%/TTT2Recomp`. Recovery files are kept outside the game folder.
No disc image or game assets are supplied.

## What changed

- Standard Windows update wizard, visible version and feature notes.
- Native game startup without the developer CMD window; normal file logging.
- Existing shortcut retained, without duplicate launcher or preview-save folders
  inside the game installation.
- Checksum validation, preserved originals and rollback on update failure.

## Current status

This remains a prerelease. The reported 39–45 FPS slowdown still needs a
same-scene retest. Fresh gameplay, cheats and live online acceptance are pending.
See the [changelog](CHANGELOG.md) and [release notes](docs/releases/0.1.7-community.4.md)
for validation and limitations.

Older experimental installers are retired. Their
[scan history](docs/graphics/ANTIVIRUS_REVIEW_2026-10-29.md) is retained; the earlier
alert has not been declared a false positive.

[Build instructions](BUILDING.md) · [Source contribution](https://github.com/shihabal3amri/tekken-tag-tournament-2-pc/pull/77)
