# Launcher and offline tools — 2026-10-28

Open **TTT2 Launcher.exe** beside the game executable. Choose the game location if
needed. Changes are staged until **Save settings** or **Play game**. Close the game
before saving launcher settings. Existing keyboard bindings stay in the game’s
Options → Controller Setup → Button Settings → Keyboard screen.

## Players

Input → **Start to join (automatic)** lets the first keyboard/controller Start
claim Player 1. A different device’s Start joins Player 2. Device presence makes
VS/Pair available without automatically assigning Player 2. Keyboard Start is your
saved binding, not necessarily Enter; the local playtest uses **N**. Common front-end
menus accept joined devices; fighter and character-select input remains separate.
Legacy shared Player 1 remains available. D-pad only and left-stick deadzone are
available; analog-only and diagonal-specific tuning are not finished.

## Graphics and quality

- **Render resolution**: 16:9 internal/output sizes from 360p to 2160p. Windowed,
  borderless and exclusive fullscreen use the real Windows/DXGI paths.
- **Anti-aliasing**: Off, FXAA, or SMAA 1x HIGH. SMAA is spatial anti-aliasing;
  it is not temporal reconstruction. Additional passes cost GPU time/memory.
- **Sharpness**: contrast-adaptive sharpening. High values may emphasize edges.
- **Texture filtering**: original or anisotropic 2x/4x/8x/16x for eligible textures.
- **Shadows**: original cast shadows on/off. No selectable shadow-resolution tiers.
- **VSync**: real presentation behavior. Windows composition may govern borderless
  presentation. Simulation remains 60 Hz with either choice.
- **Internal render scale**: follow resolution, or 50–200% of native 720p. This
  reallocates internal targets independently of output size; it also affects guest UI.
- **Mip texture detail**: original, or 1–3 coarser mip levels. This changes sampling,
  not allocated texture memory. Unmipped textures retain their original behavior.
- **Motion blur**: follow the game save, off, or on. Applied through the original
  game option after profile load. In-game changes update the launcher preference.

Original, Performance and Enhanced are concrete presets, not hardware performance
promises. They stage resolution, AA, sharpening, filtering, shadows, mip detail,
render-scale following and neutral calibration. Manual changes select Custom.

## Display

SDR brightness, gamma adjustment and contrast default to **100%**, preserving the
original image. They are real display-shader controls. This build has no HDR pipeline.
GPU choices enumerate actual adapters and require restart. Automatic prefers the
high-performance adapter; an unavailable saved index falls back to automatic.
Monitor choices enumerate actual Windows device names. Exclusive refresh choices
are OS modes matching the selected monitor/resolution, shown as integer Hz.
Windowed/borderless use desktop refresh. A refused exclusive mode reverts to automatic.
In-game mode/resolution/refresh changes have a 15-second Keep/Revert transaction.

## Diagnostics

Optional readouts appear in the **window title**; detailed mode also writes the log.
Submitted FPS counts accepted DXGI submissions, not guaranteed physical scanouts.
Render-thread CPU comes from Windows thread timing; submit wall time includes waits.
GPU interval comes from asynchronous timestamps and includes command gaps. Local video
memory is this process’s DXGI usage and budget, not invented total GPU consumption.
The title is hidden in borderless/fullscreen; use the log for detailed results there.

## Offline cheats

Cheats → **L3 + R3 overlay: On** enables the in-game cheat panel. Press both stick
buttons on the same controller. Up/Down selects; A changes; B closes.

- **Infinite health**: Off / Player 1 / Player 2 / Both sides. A side includes its
  tag partner. The damage routine refills protected health and prevents positive damage.
- **Infinite money**: refills the spendable wallet to the game’s 999,999,999 cap when
  the game resolves the wallet record. Original saving owns persistence. Disabling
  stops refills; it does not remove money already saved. Lifetime earnings are untouched.
- **Unlock content**: temporary progression/ownership query overrides for existing
  movies/rewards, wardrobe, LEDs and panels. Disabling restores ordinary availability
  checks; equipped items may be saved normally by the game. Missing assets and DLC
  licences are not supplied. All special-content/print-pattern paths are not verified.
  The original level-3 title-storage character unlock path remains enabled.

Every cheat hook checks the active-session guard, and the panel closes in online UI.
Actual live Steam acceptance is still pending because this development build lacks
Steamworks SDK support. Keep the original installed game for its existing online use.

The complete 153-ID scope and dependencies are in FEATURE_MATRIX.md. Ray tracing,
vendor reconstruction/frame generation and unmapped guest effects have no fake toggles.


## Downloadable offline preview update

Extract the entire community preview ZIP and open **TTT2 Offline Update.exe**.
Select the executable from your existing installed game when asked. It checks TU3
compatibility and creates an isolated preview with copied settings/saves. The original
installed game remains available for its existing online features. Reopen the update
bootstrap for later preview sessions; keep the original game-data folder installed.
This preview has no Steam integration, uses loopback networking, and does not sync
preview saves back into the original save folder.
