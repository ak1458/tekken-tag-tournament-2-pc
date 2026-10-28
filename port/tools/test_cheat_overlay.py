"""Production overlay state transitions with mocked UI/session, isolated INI."""
from pathlib import Path
import tempfile,os,subprocess
from test_vcmpgtuh import ROOT,compile_one
CODE=r'''
#include "cheat_overlay.cpp"
#include <cstdio>
namespace offline_cheats { int health=0;bool money=false,gate=false,unlock=false; int HealthSides(){return health;}void SetHealthSides(int v){health=v;}bool InfiniteMoney(){return money;}void SetInfiniteMoney(bool v){money=v;}void SetOfflineMenu(bool v){gate=v;}bool UnlockContent(){return unlock;}void SetUnlockContent(bool v){unlock=v;} }
bool online=false,down=false,busy=false,delay=false,shadows=true;
unsigned opened=0,dismissed=0;SysUiMessageBox current;
bool XSessionAnyActive(){return online;}
bool HostCheatOverlayChord(){return down;}
bool SysUiBoxBusy(){return busy;}
bool SysUiShowMessageBox(SysUiMessageBox box){if(busy)return false;current=std::move(box);busy=true;++opened;return true;}
void SysUiDismissBox(){busy=false;++dismissed;}
namespace display_settings {
bool GetInputDelayOn(){return delay;}void SetInputDelayOn(bool v){delay=v;}
bool GetShadows(){return shadows;}void SetShadows(bool v){shadows=v;}
}
#define CHECK(x) do{++checks;if(!(x)){printf("FAIL %d\n",__LINE__);return 1;}}while(0)
int main(){unsigned checks=0;
CheatOverlayChord c;CHECK(!c.Update(false));CHECK(c.Update(true));CHECK(!c.Update(true));CHECK(!c.Update(false));CHECK(c.Update(true));
CHECK(CheatOverlayAllowed(false,false));CHECK(!CheatOverlayAllowed(true,false));CHECK(!CheatOverlayAllowed(false,true));
cheat_overlay::Frame("FrameMainMenu");CHECK(opened==0);
down=true;cheat_overlay::Frame("FrameMainMenu");CHECK(opened==1&&busy);CHECK(cheat_overlay::ConsumeChord());
cheat_overlay::Frame("FrameMainMenu");CHECK(opened==1);
online=true;cheat_overlay::Frame("FrameMainMenu");CHECK(!busy&&dismissed==1);CHECK(!cheat_overlay::ConsumeChord());
current.done(0);CHECK(offline_cheats::health==0);
online=false;down=false;cheat_overlay::Frame("FrameMainMenu");down=true;cheat_overlay::Frame("FrameOnlineMenu");CHECK(opened==1);
down=false;cheat_overlay::Frame("FrameMainMenu");down=true;cheat_overlay::Frame("FrameMainMenu");CHECK(opened==2);
busy=false;current.done(0);CHECK(offline_cheats::health==1);down=false;cheat_overlay::Frame("FrameMainMenu");CHECK(opened==3);
busy=false;current.done(3);cheat_overlay::Frame("FrameMainMenu");CHECK(!busy);
printf("PASS %u overlay checks: chord edges, busy UI, online closure, stale callback guard, offline action\n",checks);
}
'''
with tempfile.TemporaryDirectory(prefix='ttt2-overlay-') as temp:
 folder=Path(temp);exe=compile_one(folder,'overlay',CODE,[ROOT/'port/src/runtime/kernel'])
 ini=folder/'settings.ini';ini.write_text('[Mods]\nOverlay=1\n')
 subprocess.run([str(exe)],env=dict(os.environ,TTT2_SETTINGS_INI=str(ini)),check=True)
