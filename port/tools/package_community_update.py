"""Create an explicitly offline, asset-free preview update ZIP from local builds."""
import argparse,hashlib,json,subprocess,zipfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
README="""TTT2 Windows community offline preview — 2026-10-28

This is an unofficial experimental preview based on upstream v0.1.7.
It is NOT an in-place replacement for the official installed game.
Steam online is not compiled into this preview. Keep the original for online play.

1. Close the game and launcher. Extract this entire ZIP into an ordinary folder.
2. Open "TTT2 Offline Update.exe".
3. Select your EXISTING "Tekken Tag Tournament 2.exe" when asked.
4. The update checks the USA/Europe TU3 image, checks payload hashes, copies your
   existing settings and saves into a separate preview folder, then opens the launcher.
5. Use the launcher to select input, graphics and offline cheats, then Play Game.
   Reopen "TTT2 Offline Update.exe" for subsequent preview sessions.

The original installation, executable, settings and saves are never overwritten.
The preview reads your existing assets; keep that original game folder installed.
Preview changes do not sync back to original saves. Later runs retain preview saves.
No ISO, XEX, title-update files, tekken.img, assets, user settings/saves or SDK headers
are included in this download. A small boot image and VC runtime DLLs are copied
locally from your existing installation; game assets are reused in place.

Preview state: %LOCALAPPDATA%/TTT2RecompCommunityPreview/v0.1.7-community.1
Returning to the original: close the preview and use your normal game shortcut.

Included: native launcher with original generated arena art; first-Start player
ownership; separate keyboard/controller joining; SOCD/deadzone; SMAA 1x; actual SDR
calibration, adapter/monitor/exclusive-refresh choices, render scale/mip detail,
optional performance readout; L3+R3 offline health/money/content controls.

Health's latest address-guard fix passes 238 automated checks and a negative control;
live fight acceptance of that corrected binary remains pending. Money/unlock/overlay
were user-tested. Full online/rollback, multi-monitor and graphics benchmark acceptance
is incomplete. Unlocks are temporary checks for installed content; missing DLC/assets
are not supplied. This does not implement all 153 requested graphics technologies.

SMAA attribution/licence: LICENSES/SMAA-LICENSE.txt and LICENSES/SMAA-README.md.
The preview updater and ZIP are unsigned. Checksums detect corruption, not publisher
identity. Download only from the contributor release linked in the pull request.
"""

def digest(path):
    with path.open('rb') as stream:return hashlib.file_digest(stream,'sha256').hexdigest()

def stage(output,game,launcher,bootstrap):
    output.mkdir(parents=True,exist_ok=True);(output/'bin').mkdir(exist_ok=True);(output/'LICENSES').mkdir(exist_ok=True)
    import shutil
    mapping={'bin/game.exe':game,'bin/launcher.exe':launcher,'TTT2 Offline Update.exe':bootstrap,
             'LICENSES/SMAA-LICENSE.txt':ROOT/'port/third_party/smaa/LICENSE.txt',
             'LICENSES/SMAA-README.md':ROOT/'port/third_party/smaa/README.md'}
    for name,path in mapping.items():
        if not path.is_file():raise FileNotFoundError(path)
        shutil.copy2(path,output/name)
    (output/'payload.sha256').write_text(''.join(digest(output/'bin'/name)+'  '+name+'\n' for name in ('game.exe','launcher.exe')))
    (output/'README.txt').write_text(README,encoding='utf-8')
    revision=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()
    (output/'build-info.json').write_text(json.dumps({'version':'v0.1.7-community.1','base':'v0.1.7','source_revision':revision,
        'platform':'windows-x64','steam_enabled':False,'experimental':True,'game_assets_included':False},indent=2)+'\n')
    return list(mapping)+['payload.sha256','README.txt','build-info.json']

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--game',type=Path,default=ROOT/'port/build-o1/tekken_recomp.exe')
    parser.add_argument('--launcher',type=Path,default=ROOT/'port/build-launcher/TTT2 Launcher.exe')
    parser.add_argument('--bootstrap',type=Path,default=ROOT/'port/build-launcher/TTT2 Offline Update.exe')
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();folder=args.output.resolve()
    entries=stage(folder,args.game,args.launcher,args.bootstrap)
    archive=folder.parent/(folder.name+'.zip')
    with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as package:
        for name in entries:package.write(folder/name,name)
    checksum=archive.with_suffix('.zip.sha256');checksum.write_text(digest(archive)+'  '+archive.name+'\n')
    with zipfile.ZipFile(archive) as package:
        assert set(package.namelist())==set(entries)
        assert package.testzip() is None
    print(archive);print(checksum);print('Verified archive allowlist:',len(entries),'entries; no game assets or personal files')

if __name__=='__main__':main()
