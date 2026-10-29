#pragma once
#ifndef NOMINMAX
#define NOMINMAX
#endif
#include <windows.h>
#include <filesystem>
#include <fstream>
#include <stdexcept>
#include <string>

// The installed launcher restores its own isolated environment. A desktop link
// can target it directly; the downloaded updater is needed only to install updates.
namespace preview_environment {
inline bool Configure(const std::filesystem::path& executable) {
    namespace fs=std::filesystem;
    const auto app=fs::absolute(executable).lexically_normal().parent_path();
    const auto state=app.parent_path();
    const auto marker=state/L".ttt2-community-preview-v1";
    if(app.filename()!=L"app" || !fs::is_regular_file(marker))return false;
    std::ifstream stream(marker);std::string value;std::getline(stream,value);
    if(value!="TTT2 community offline preview v1")
        throw std::runtime_error("Invalid offline preview. Run the updater again.");
    wchar_t installed[32768]{};
    GetPrivateProfileStringW(L"Preview",L"InstalledGame",L"",installed,32768,(state/L"preview.ini").c_str());
    const fs::path assets=fs::path(installed)/L"game";
    if(!*installed || !fs::is_regular_file(assets/L"tekken.img") ||
       !fs::is_regular_file(app/L"tekken_recomp.exe") ||
       !fs::is_regular_file(state/L"settings.ini") || !fs::is_directory(state/L"saves"))
        throw std::runtime_error("Offline preview files or original game assets are missing. Run the updater and select the original game again.");
    if(!SetEnvironmentVariableW(L"TTT2_SETTINGS_INI",(state/L"settings.ini").c_str()) ||
       !SetEnvironmentVariableW(L"TTT2_SAVE_ROOT",(state/L"saves").c_str()) ||
       !SetEnvironmentVariableW(L"TTT2_VFS_ROOT",assets.c_str()) ||
       !SetEnvironmentVariableW(L"TTT2_NET",L"loopback"))
        throw std::runtime_error("Cannot configure the offline preview environment.");
    SetEnvironmentVariableW(L"TTT2_INPUT_SCRIPT",nullptr);
    SetEnvironmentVariableW(L"TTT2_AUTOSTART",nullptr);
    return true;
}
}
