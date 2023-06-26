# programs.py

def get(program_number):
    program_mapping = {
        1: {
            'name': "Opera GXSetup",
            'download_link': "https://net.geo.opera.com/opera_gx/stable/windows?utm_tryagain=yes&&&&gclsrc=aw.ds&&gclid=CjwKCAjwyqWkBhBMEiwAp2yUFpfGFEyk3m4D03eiZc6jCVWVsm0sdhgJqmJfg7ESnwA-b0_67rk0OBoCfgUQAvD_BwE&http_referrer=https%3A%2F%2Fwww.google.com%2F&utm_site=opera_com&&utm_lastpage=opera.com/gx/gx-browser"
        },
        2: {
            'name': "ChromeSetup",
            'download_link': "https://dl.google.com/tag/s/appguid%3D%7B8A69D345-D564-463C-AFF1-A69D9E530F96%7D%26iid%3D%7B313F249D-415F-CEE3-9E10-219FD77D5FED%7D%26lang%3Dde%26browser%3D4%26usagestats%3D1%26appname%3DGoogle%2520Chrome%26needsadmin%3Dprefers%26ap%3Dx64-stable-statsdef_1%26installdataindex%3Dempty/update2/installers/ChromeSetup.exe"
        },
        3: {
            'name': "FirefoxSetup",
            'download_link': "https://download.mozilla.org/?product=firefox-stub&os=win&lang=de&attribution_code=c291cmNlPXd3dy5nb29nbGUuY29tJm1lZGl1bT1yZWZlcnJhbCZjYW1wYWlnbj0obm90IHNldCkmY29udGVudD0obm90IHNldCkmZXhwZXJpbWVudD0obm90IHNldCkmdmFyaWF0aW9uPShub3Qgc2V0KSZ1YT1jaHJvbWUmY2xpZW50X2lkPTIxNDMyMzAwOC4xNjg2NzUzMzQ4JnNlc3Npb25faWQ9MjMwOTMwODk2MSZkbHNvdXJjZT1tb3pvcmc.&attribution_sig=fd653a2c27726c02bc71fb9f44451870c62f387235d469a4fda526ce5dd5c9b9&_gl=1*1l7mpx9*_ga*MjE0MzIzMDA4LjE2ODY3NTMzNDg.*_ga_MQ7767QQQW*MTY4Njc1MzM0OC4xLjEuMTY4Njc1MzM1NS4wLjAuMA.."
        },
        4: {
            'name': "OperaSetup",
            'download_link': "https://net.geo.opera.com/opera/stable/windows?utm_tryagain=yes&&&&gclsrc=aw.ds&&gclid=CjwKCAjwyqWkBhBMEiwAp2yUFpfGFEyk3m4D03eiZc6jCVWVsm0sdhgJqmJfg7ESnwA-b0_67rk0OBoCfgUQAvD_BwE&http_referrer=https%3A%2F%2Fwww.google.com%2F&utm_site=opera_com&"
        },
        5: {
            'name': "BraveSetup",
            'download_link': "https://referrals.brave.com/latest/BraveBrowserSetup-BRV002.exe"
        },
        6: {
            'name': "TorSetup",
            'download_link': "https://www.torproject.org/dist/torbrowser/12.0.7/torbrowser-install-win64-12.0.7_ALL.exe"
        },
        7: {
            'name': "MinecraftSetup",
            'download_link': "https://launcher.mojang.com/download/MinecraftInstaller.exe"
        },
        8: {
            'name': "RobloxSetup",
            'download_link': "https://www.roblox.com/download/client"
        },
        9: {
            'name': "SteamSetup",
            'download_link': "https://cdn.akamai.steamstatic.com/client/installer/SteamSetup.exe"
        },
        10: {
            'name': "EpicGamesSetup",
            'download_link': "https://launcher-public-service-prod06.ol.epicgames.com/launcher/api/installer/download/EpicGamesLauncherInstaller.msi"
        },
        11: {
            'name': "OriginSetup",
            'download_link': "http://www.dm.origin.com/download"
        },
        12: {
            'name': "UplaySetup",
            'download_link': "https://ubi.li/4vxt9"
        },
        13: {
            'name': "DiscordSetup",
            'download_link': "https://discord.com/api/downloads/distributions/app/installers/latest?channel=stable&platform=win&arch=x86"
        },
        14: {
            'name': "SkypeSetup",
            'download_link': "https://go.skype.com/skype.download"
        },
        15: {
            'name': "ZoomSetup",
            'download_link': "https://zoom.us/client/5.14.11.17466/ZoomInstallerFull.exe?archType=x64"
        },
        16: {
            'name': "MsTeamsSetup",
            'download_link': "https://go.microsoft.com/fwlink/?linkid=2187217&Lmsrc=groupChatMarketingPageWeb&Cmpid=directDownloadv2Win64"
        },
        17: {
            'name': "Ts3Setup",
            'download_link': "https://dl.4players.de/ts/releases/3.5.6/TeamSpeak3-Client-win64-3.5.6.exe?_ga=2.66128622.1563628100.1686776527-390382963.1686776526"
        },
        18: {
            'name': "WhatsAppSetup",
            'download_link': "https://r2.computerbild.de/exec/r2r.pl?m=w-cobi;u=https%3A%2F%2Fd.computerbild.de%2Fdownloads%2F8055805%2FWhatsAppSetup.exe%3F__cbodl__%3D1686777812_d91a3d244c3a5880e70849a1bf103e6c%26_chksum_%3D575f44cc710b76987dd99a5a6adb21ab;ct=1;thc=1;b=8055805;c=15682211;tit=WhatsApp+f%C3%BCr+PC+%2864-Bit-Desktop-App%29%0A;url=https%3A%2F%2Fwww.computerbild.de;sep=%7C;tce=%7C;tid=482;tn=Chat-Programme+%26+Messenger;tp=95%7C364;tc=95%7C364%7C482;tpn=Downloads%7CInternet;cs=1;chk=6bc21ae72df9d353"
        },
        19: {
            'name': "GeforceExperienceSetup",
            'download_link': "https://de.download.nvidia.com/GFE/GFEClient/3.27.0.112/GeForce_Experience_v3.27.0.112.exe"
        },
        20: {
            'name': "AMDDriverSetup",
            'download_link': "https://drivers.amd.com/drivers/installer/22.40/whql/amd-software-adrenalin-edition-23.5.2-minimalsetup-230531_web.exe"
        },
        21: {
            'name': "DSASetup",
            'download_link': "https://dsadata.intel.com/installer"
        },
        22: {
            'name': "WinAudioDrvSetup",
            'download_link': "https://downloadmirror.intel.com/27879/Audio-Win10_Win11-6.0.9456.1.zip"
        },
        23: {
            'name': "DS4WindowsSetup",
            'download_link': "https://github.com/Ryochan7/DS4Windows/releases/download/v3.2.11/DS4Windows_3.2.11_x64.zip"
        },
        24: {
            'name': "NetworkAdapterDrvSetup",
            'download_link': "https://downloadmirror.intel.com/772070/Wired_driver_28.0_x64.zip"
        },
        25: {
            'name': "7ZipSetup",
            'download_link': "https://7-zip.org/a/7z2300-x64.exe"
        },
        26: {
            'name': "WinRARSetup",
            'download_link': "https://www.rarlab.com/rar/winrar-x64-622.exe"
        },
        27: {
            'name': "CCleanerSetup",
            'download_link': "https://bits.avcdn.net/productfamily_CCLEANER/insttype_FREE/platform_WIN_PIR/installertype_ONLINE/build_RELEASE/cookie_mmm_ccl_012_999_a7f_m"
        },
        28: {
            'name': "MalwarebytesSetup",
            'download_link': "https://www.malwarebytes.com/api/downloads/mb-windows?filename=MBSetup.exe"
        },
        29: {
            'name': "ProtonVPNSetup",
            'download_link': "https://protonvpn.com/download/ProtonVPN_v3.0.5.exe"
        },
        30: {
            'name': "RevoSetup",
            'download_link': "https://download.revouninstaller.com/download/revosetup.exe"
        },
    }

    return program_mapping.get(program_number)
