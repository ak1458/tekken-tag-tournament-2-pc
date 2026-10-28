#define WIN32_LEAN_AND_MEAN
#include <windows.h>
#include "cheat_overlay.h"
#include "cheat_overlay_policy.h"
#include "sys_ui.h"
#include "display_settings.h"
#include "offline_cheats.h"
#include <cstdlib>
#include <string>
#include <atomic>
bool XSessionAnyActive();
namespace cheat_overlay {
namespace {
CheatOverlayChord chord;
bool owned = false;
bool reopen = false;
std::string lastFrame;
std::atomic<bool> offlineGate{false};
bool Offline() { return CheatOverlayAllowed(lastFrame.rfind("FrameOnline",0)==0,XSessionAnyActive()); }
void Open() {
    if (!Offline() || SysUiBoxBusy()) return;
    SysUiMessageBox box;
    box.text = "OFFLINE CHEATS\nUP/DOWN: select | A: change | B: close\nUnlocks affect existing installed content only.";
    static const char* healthNames[]={"Off","Player 1","Player 2","Both sides"};
    box.buttons = {
        std::string("Infinite health: ")+healthNames[offline_cheats::HealthSides()],
        std::string("Infinite money: ")+(offline_cheats::InfiniteMoney()?"ON":"OFF"),
        std::string("Unlock content: ")+(offline_cheats::UnlockContent()?"ON":"OFF"),
        "Close"
    };
    box.cancel = 3;
    box.done = [](int choice) {
        owned = false;
        if (!Offline()) return;
        if (choice == 0) offline_cheats::SetHealthSides((offline_cheats::HealthSides()+1)%4);
        if (choice == 1) offline_cheats::SetInfiniteMoney(!offline_cheats::InfiniteMoney());
        if (choice == 2) offline_cheats::SetUnlockContent(!offline_cheats::UnlockContent());
        reopen = choice >=0 && choice < 3;
    };
    owned = SysUiShowMessageBox(std::move(box));
}
}
bool Enabled() {
    static const bool enabled = [] {
        const char* overridePath=std::getenv("TTT2_SETTINGS_INI");
        char local[MAX_PATH]{};GetEnvironmentVariableA("LOCALAPPDATA",local,MAX_PATH);
        const std::string path=overridePath&&*overridePath?overridePath:std::string(local)+"\\TTT2Recomp\\settings.ini";
        return GetPrivateProfileIntA("Mods","Overlay",0,path.c_str())==1;
    }();
    return enabled;
}
bool ConsumeChord() { return Enabled() && offlineGate.load(); }
void Frame(const std::string& currentFrame) {
    lastFrame=currentFrame;
    offlineGate.store(Offline());
    offline_cheats::SetOfflineMenu(Offline());
    const bool pressed=chord.Update(HostCheatOverlayChord());
    if (!Enabled()) return;
    if (!Offline()) {
        reopen=false;
        if (owned) { SysUiDismissBox();owned=false; }
        return;
    }
    if (reopen && !SysUiBoxBusy()) { reopen=false;Open(); }
    if (pressed && !SysUiBoxBusy()) Open();
}
}
