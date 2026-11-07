# Tekken Tag Tournament 2 — Community Windows Update

[![Release: Prerelease](https://img.shields.io/badge/Release-Prerelease-D97706?style=flat-square)](https://github.com/ak1458/tekken-tag-tournament-2-pc/releases)
[![Source: Community fork](https://img.shields.io/badge/Source-Community%20fork-64748B?style=flat-square)](https://github.com/shihabal3amri/tekken-tag-tournament-2-pc)

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


## Source architecture

This is a community fork of the upstream static-recompilation project. It adds Windows update/launcher and graphics/input work around an existing game installation. The original port and other contributors retain their credit.

| Area | Purpose |
| --- | --- |
| [port/](port/) | Native runtime and platform build source. |
| [tools/](tools/) | Build, packaging, patch, and preparation helpers. |
| [server/](server/) | Online/server protocol implementation and notices. |
| [docs/graphics/](docs/graphics/) | Renderer/input research and validation records. |
| [BUILDING.md](BUILDING.md) | Required toolchain and owner-supplied game-file build path. |

## Build and validate

Read [BUILDING.md](BUILDING.md) before compiling. Its toolchain includes Visual Studio 2022 Build Tools, LLVM/Clang, CMake/Ninja, Python, and generated C++ from the owner’s disc image and title update. Recompiler/runtime dependencies and paths are documented there. The repository does not supply game assets, an Xbox title update, or a Steamworks SDK.

The optional launcher can be built using `tools\build_launcher.cmd`. Device-routing checks include `python port/tools/test_separate_players.py`; these use simulated input and do not establish gameplay or online acceptance. Graphics checks and their platform requirements are documented under `docs/graphics/`.

## Version and distribution notes

The published updater is **v0.1.7-community.4**, marked as a prerelease. Its installer and checksum are actual GitHub release assets. A source archive, launcher build, game installation, and binary updater are different artifacts; use the instructions for the artifact you intend to run. No GitHub Packages artifact is implied.

## Licensing and notices

No root blanket project license is present in this fork. Preserve upstream, bundled dependency, server, renderer, and third-party notices. Availability of source or an updater does not grant rights to game content. See the upstream project and relevant notices before redistribution.
