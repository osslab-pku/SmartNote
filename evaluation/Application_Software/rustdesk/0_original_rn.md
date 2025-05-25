![image](https://github.com/rustdesk/rustdesk/assets/71636191/83754a64-31b8-47f0-8570-da22207759a9)

| Architecture | Windows | Ubuntu | Mac | Android | Flatpak | AppImage | iOS |
|--------------|---------|--------|-----|----------|---------|---------|---------|
| x86-64 (64-bit) | [EXE](https://github.com/rustdesk/rustdesk/releases/download/1.3.0/rustdesk-1.3.0-x86_64.exe) &nbsp; [MSI](https://github.com/rustdesk/rustdesk/releases/download/1.3.0/rustdesk-1.3.0-x86_64.msi) | [Download](https://github.com/rustdesk/rustdesk/releases/download/1.3.0/rustdesk-1.3.0-x86_64.deb) | [Download](https://github.com/rustdesk/rustdesk/releases/download/1.3.0/rustdesk-1.3.0-x86_64.dmg) | [Universal](https://github.com/rustdesk/rustdesk/releases/download/1.3.0/rustdesk-1.3.0-universal-signed.apk) | [Download](https://github.com/rustdesk/rustdesk/releases/download/1.3.0/rustdesk-1.3.0-x86_64.flatpak) | [Download](https://github.com/rustdesk/rustdesk/releases/download/1.3.0/rustdesk-1.3.0-x86_64.AppImage) |
| AArch64 (ARM64) |  | [Download](https://github.com/rustdesk/rustdesk/releases/download/1.3.0/rustdesk-1.3.0-aarch64.deb) | [Download](https://github.com/rustdesk/rustdesk/releases/download/1.3.0/rustdesk-1.3.0-aarch64.dmg) | [Download](https://github.com/rustdesk/rustdesk/releases/download/1.3.0/rustdesk-1.3.0-aarch64-signed.apk) | [Download](https://github.com/rustdesk/rustdesk/releases/download/1.3.0/rustdesk-1.3.0-aarch64.flatpak) |  [Download](https://github.com/rustdesk/rustdesk/releases/download/1.3.0/rustdesk-1.3.0-aarch64.AppImage)  | [TestFlight](https://testflight.apple.com/join/KBG9EsZW)
| ARMv7 (32-bit) |  | [Download](https://github.com/rustdesk/rustdesk/releases/download/1.3.0/rustdesk-1.3.0-armv7-sciter.deb) |  |  [Download](https://github.com/rustdesk/rustdesk/releases/download/1.3.0/rustdesk-1.3.0-armv7-signed.apk) |  |  |
| x86-32 (32-bit) | [Download](https://github.com/rustdesk/rustdesk/releases/download/1.3.0/rustdesk-1.3.0-x86-sciter.exe) |  |  |  |  |  |


## For more downloads (Fedora / Arch Linux / Suse): [check below please](#)

## For the latest features: [check out the nightly build](https://github.com/rustdesk/rustdesk/releases/tag/nightly)

 <details>
 <summary>Changelog</summary>

# Added
- Multi clipboard formats, html/rtf ([#8733](https://github.com/rustdesk/rustdesk/pull/8733))
- Send clipboard keystroke ([#5451](https://github.com/rustdesk/rustdesk/discussions/5451))
- Active tab border ([#8832](https://github.com/rustdesk/rustdesk/discussions/8832))
- MSI options of creation of desktop and start menu shortcuts ([#8829](https://github.com/rustdesk/rustdesk/discussions/8829))
- Add client to address book/tag via command line ([#7866](https://github.com/rustdesk/rustdesk/discussions/7866))
- Universal apk, ARM64 / ARM32 / X86_64 ([#8941](https://github.com/rustdesk/rustdesk/pull/8941))
- Unlock with pin ([#7656](https://github.com/rustdesk/rustdesk/discussions/7656))
- `Trust this device` option for 2FA ([#8513](https://github.com/rustdesk/rustdesk/discussions/8513))
- Rename File and Folder in file transfer window ([#7758](https://github.com/rustdesk/rustdesk/discussions/7758))

# Changed
- Keep window pos after new conn ([#8834](https://github.com/rustdesk/rustdesk/pull/8834))
- Vcpkg ffmpeg ([#8764](https://github.com/rustdesk/rustdesk/pull/8764))
- Remove autostart entry of `--tray` on Linux ([#4863](https://github.com/rustdesk/rustdesk/issues/4863))
- Use JNI MediaCodec-backed hardware codecs on Android which may fix some `waiting for image`  ([#8985](https://github.com/rustdesk/rustdesk/pull/8985))
- Remove virtual displays on disconnection ([#8044](https://github.com/rustdesk/rustdesk/discussions/8044))

# Fixed
- Reversed left/right wheel  ([#1169](https://github.com/rustdesk/rustdesk/issues/1169))
- Huge memory usage ([#8883](https://github.com/rustdesk/rustdesk/issues/8883))
- Audio latency accumulation ([#534](https://github.com/rustdesk/rustdesk/issues/534))
- Sciter incompatible with stable Rust ([#8856](https://github.com/rustdesk/rustdesk/issues/8856))
- Doesn't pick Ukrainian translation by default ([#8923](https://github.com/rustdesk/rustdesk/issues/8923))
- Trackpad, reverse horizontal scroll ([#8827](https://github.com/rustdesk/rustdesk/pull/8827))
- Debian unable to unlock settings ([#8719](https://github.com/rustdesk/rustdesk/issues/8719))
- After maximizing the control window, the active bar of the Windows taskbar icon cannot be seen ([#8979](https://github.com/rustdesk/rustdesk/issues/8979))
- Privacy mode 2 not work ([#8994](https://github.com/rustdesk/rustdesk/discussions/8994))
- Cannot connect with allow-remove-wallpaper enabled ([#9053](https://github.com/rustdesk/rustdesk/discussions/9053))
- Top edge resize on WIndows ([#9081](https://github.com/rustdesk/rustdesk/pull/9081))
- Dock icon frequently bouncing on macOS ([#9088](https://github.com/rustdesk/rustdesk/issues/9088))
- Clipboard logic still broken (multiple connections) ([#7321](https://github.com/rustdesk/rustdesk/issues/7321))
- Crash on fedora ([#9051](https://github.com/rustdesk/rustdesk/issues/9051))

</details>
