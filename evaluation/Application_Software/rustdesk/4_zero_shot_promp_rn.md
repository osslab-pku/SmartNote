# Release Notes for Version 1.3.0

## New Features
- **Clipboard Multi-Format Support**: Added support for multiple clipboard formats including text, RTF, HTML, PNG, and SVG. This feature enhances the clipboard functionality by allowing more data types to be transferred between sessions.
- **Trusted Devices for 2FA**: Introduced a feature to trust devices to skip 2FA verification, improving user convenience while maintaining security.
- **Unlock with PIN**: Users can now set a custom PIN to unlock settings, providing an additional layer of security.

## Enhancements
- **Android Hardware Codec**: Utilized JNI MediaCodec-backed hardware codecs on Android for improved performance and compatibility.
- **Audio Buffer Management**: Set the maximum audio buffer to 150ms and implemented buffer clearing if full, reducing audio delay caused by network jitter.
- **Privacy Mode Improvements**: Enhanced privacy mode with better error handling and resolution management, especially for Windows virtual displays.
- **UI and UX Improvements**: Various UI enhancements including tooltip additions, dialog content improvements, and better handling of window resizing and positioning.

## Bug Fixes
- **Clipboard Handling**: Fixed issues with clipboard data handling, ensuring more reliable data transfer and format recognition.
- **Connection Stability**: Addressed several connection stability issues, including those related to network errors and session management.
- **Build and CI Fixes**: Resolved build issues on various platforms, including fixing CI failures related to MSVCRT conflicts on Windows.
- **Language and Localization**: Updated translations and fixed typos across multiple languages, improving the overall user experience for non-English users.

## Technical Improvements
- **VCPKG Dependencies**: Updated VCPKG dependencies, including a bump to Opus 1.5.2 and improvements to the build process for better performance and reliability.
- **Code Refactoring**: Significant refactoring of the codebase to improve maintainability and performance, including updates to the clipboard service and input handling.

## Known Issues
- **Wayland Support**: Wayland support is still experimental and may not work as expected on all systems. Users are advised to use X11 for better compatibility.

This release brings significant improvements in functionality, performance, and user experience. Users are encouraged to update to take advantage of the new features and enhancements.