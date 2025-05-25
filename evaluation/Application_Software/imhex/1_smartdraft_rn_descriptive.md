# v1.35.4
## 🐛 fix
- The updater executable now launches correctly even when the path contains spaces. [c922d9c](https://github.com/WerWolv/ImHex/commit/c922d9ceecb143b4793e3b84da448a8dd24a590d) 
- Improved to prevent canvas flickering in the web build. [b305adb](https://github.com/WerWolv/ImHex/commit/b305adb2866b3d6291ff4c5db0b2ae5186934263) 
- Addresses issues with the ImHex logo and the default fill of the progress bar on the web interface. Improved logo size on mobile. [67930cf](https://github.com/WerWolv/ImHex/commit/67930cf65de72db95d913a25895a9c938f86d9a7) [84999d5](https://github.com/WerWolv/ImHex/commit/84999d5c068467ea97a7bb120dc22bd383bd9d26)
- Eliminated window resize flickering on Windows for improved user experience. [5fced6b](https://github.com/WerWolv/ImHex/commit/5fced6bb63b8858611383639d0de0c873557fcba) [ad235fa](https://github.com/WerWolv/ImHex/commit/ad235fad25ddb1e355c4843f732b9df0799db345)
- Updated the about page to include Boost.Regex. [c6fc26e](https://github.com/WerWolv/ImHex/commit/c6fc26e2e75ecc0a4a9f5c331bfcf80843957721) 
- Fixed a potential race condition with sorting in the pattern drawer. [dd8e702](https://github.com/WerWolv/ImHex/commit/dd8e7025d037b424caedb702571cb36f7a919528) 
- Disabled tab overlines by setting `ImGuiCol_TabSelectedOverline` and `ImGuiCol_TabDimmedSelectedOverline` colors to transparent. [6784678](https://github.com/WerWolv/ImHex/commit/6784678ff0aca040491fa8a374ab46b36768a9d2) 
- Improved WebGL context creation logic in the canvas element, with better handling of context loss and fallback mechanisms for WebGL 2 support. [3b79938](https://github.com/WerWolv/ImHex/commit/3b799388c25db45855688deb55f4648fb62ee7a3) 
- Added a user-friendly console warning to notify when the .NET runtime is not installed. [dd0204f](https://github.com/WerWolv/ImHex/commit/dd0204f31df334f3424faaa27d2ed648f30bc965) 
- Removed debug code from the interactive help menu. [d5a69d9](https://github.com/WerWolv/ImHex/commit/d5a69d9201878bd5b436c4631bba688c353543b6) 
- Tooltips added to toolbar buttons for additional information on hover. [a45d30e](https://github.com/WerWolv/ImHex/commit/a45d30edcaa282c5be5635df9d2b7ccb6dc58a51) 
- Fixed incorrect start/end offset and size for static array entries in the pattern data view. [cfbc6e0](https://github.com/WerWolv/ImHex/commit/cfbc6e085a4dda0145321bd7e197b7b7f945be6c) [c7c4eca](https://github.com/WerWolv/ImHex/commit/c7c4ecad6dfce1f1e6629d8b1e8b96960c7573e4)
- Modified event handling for mouse and touch inputs to ensure correct touch interactions, preventing issues like multiple taps for button registration and windows getting stuck during drag or resize actions. Introduced a listener to switch between mouse and touch modes, enhancing the user experience on touch-enabled devices. [1d99f85](https://github.com/WerWolv/ImHex/commit/1d99f8534ddfe89998673881e7eb330091529e2f) 
- Adjusted welcome screen behavior to ensure it always remains in the background, preventing it from coming to the front when focused. [a0ca0e8](https://github.com/WerWolv/ImHex/commit/a0ca0e859694c41b1dcd562b4281adb7374cde8f) 
- Removed unnecessary touch padding from the menu definition function. [0785270](https://github.com/WerWolv/ImHex/commit/0785270dfadb8d112c8c30d966b900fbe4fa1cc4) 
- The canvas is now fixed to the top left of the screen for consistent positioning across different screen sizes and resolutions. [c79321b](https://github.com/WerWolv/ImHex/commit/c79321b550f8d0f6dccaaee8ab3cabec65abc773) 
- Long touches on the web interface now trigger right-click actions. Right-click context menu behavior refined to prevent activation while dragging, ensuring precise interactions. [5d53417](https://github.com/WerWolv/ImHex/commit/5d534176830fda39aee0b912fe4f5997ceb083cf) 
- Fixed transparency issue in Hex editor popups when hovering over a combo box. [1c2bb0c](https://github.com/WerWolv/ImHex/commit/1c2bb0c04959549890d5d97d26c05b469f0fbcf5) 
- Fixed a crash on macOS when dirtying or undirtying a provider from a thread by using TaskManager to defer `macosMarkContentEdited` for thread safety. [22dc3c6](https://github.com/WerWolv/ImHex/commit/22dc3c65893f34a11787b8dc80b30e8b07e28400) 
- Fixed a build issue due to an uncaptured 'this' pointer in the macOS window implementation. [4d1e29d](https://github.com/WerWolv/ImHex/commit/4d1e29d7479178ac5baab9b8a0e8b2dac7170f79) 
- Pattern debug mode now disables automatically after evaluation. [8a4599f](https://github.com/WerWolv/ImHex/commit/8a4599feeadc7432462fd946d8009df3c5430557) 
- Fixed multiple plugin feature definition errors. [edb1a88](https://github.com/WerWolv/ImHex/commit/edb1a8876b5eb8cf6ba3840df3611203b91bfeac) 
- Optimized highlight hovering for better performance. [2757075](https://github.com/WerWolv/ImHex/commit/2757075a10cb9c6ac95ec83259859473765c4732)

## ✨ feat
- Improved size display in the pattern data view for a more detailed and user-friendly representation. [c7c4eca](https://github.com/WerWolv/ImHex/commit/c7c4ecad6dfce1f1e6629d8b1e8b96960c7573e4) 
- Optimized highlight hovering for better performance. [2757075](https://github.com/WerWolv/ImHex/commit/2757075a10cb9c6ac95ec83259859473765c4732) 

## 📦 build
- Updated the build system to properly locate the boost and libimhex libraries in the SDK. [cbcf7b7](https://github.com/WerWolv/ImHex/commit/cbcf7b78e9460a3211bd4b1b477eb75098aefd3c) 
- The ImGui library update introduces new features, changes input event handling, navigation, and rendering. Modifications to UI elements like tabs and sliders enhance user experience and offer more flexibility in UI customization. [3a99d53](https://github.com/WerWolv/ImHex/commit/3a99d53ba5c93e39690776037e9341f4e09b05ae) 
- File dialogs now stay on top of the main window on Windows, macOS, and Linux/X11 platforms, fixing the issue where dialogs would go behind the main window if it was clicked while open. [5a053aa](https://github.com/WerWolv/ImHex/commit/5a053aa146acd8e2dd06174faa5b7002f29d32dc) 
- Streamlined plugin feature definition by enhancing macro handling and feature definition process. Improved CMake configuration and plugin setup for more efficient management. [f8f4701](https://github.com/WerWolv/ImHex/commit/f8f47012c4c1e4b299cb48e46ef3b783b2422df2) 
- Addresses issues with lzma support and streamlines the process for building zstd. [cb406ea](https://github.com/WerWolv/ImHex/commit/cb406ea35728498e1d42b6b5d936d40900d9ce51) 
- Version updated. [811214d](https://github.com/WerWolv/ImHex/commit/811214ddb79b66dba5ca56021212f81f9d89d608) 

## 🔧 chore
- Updated the pattern language. [c2f661f](https://github.com/WerWolv/ImHex/commit/c2f661f02146d782120e9e89835be391aa04f1ee) 
- Updated the Mesa3D NoGPU version download link in the build workflow. [32e2ccb](https://github.com/WerWolv/ImHex/commit/32e2ccbca004d5b6ba62cb47a53f103c2b5d45a9)