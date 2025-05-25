# Release Notes for v1.35.4

## Overview
This release focuses on improving the user experience by addressing several bugs, enhancing performance, and updating dependencies. Key improvements include resolving window resize flickering on Windows, enhancing the web build, and updating various libraries.

## New Features and Improvements
- **Window Resize Flickering**: Completely eradicated window resize flickering on Windows, providing a smoother user experience.
- **Web Build Enhancements**: Improved canvas flickering prevention and WebGL creation logic, along with better touch input handling.
- **UI Enhancements**: Added tooltips to toolbar buttons and improved size display in the pattern data view.
- **Console Warnings**: Added a more informative console warning when the .NET runtime isn't installed.
- **Pattern Language**: Updated the pattern language for better performance and usability.
- **Boost.Regex**: Added Boost.Regex information to the about page.

## Bug Fixes
- **Updater Execution**: Fixed an issue where the updater executable was not launched correctly if the path contained spaces.
- **Pattern Drawer**: Resolved a potential race condition with sorting in the pattern drawer.
- **Hex Editor**: Fixed transparency issues with popups when hovering over combo box popups.
- **macOS Crash**: Fixed a crash on macOS when dirtying or undirtying a provider from a thread.
- **Build Issues**: Addressed build issues related to uncaptured `this` pointer and multiple definitions errors with plugin features.
- **Web Logo and Progress Bar**: Corrected the default fill for the ImHex logo and progress bar on the web version.
- **Welcome Screen**: Ensured the welcome screen always stays in the background.

## Build and Dependency Updates
- **Library Updates**: Updated ImGui, libfmt, and libyara to their latest versions.
- **Boost and libimhex**: Properly configured the build to look for Boost and libimhex libraries in the SDK.
- **Nativefiledialog**: Updated the nativefiledialog submodule to ensure dialogs stay on top of the main window across different platforms.
- **CMakeLists**: Various updates to CMakeLists for better build configuration and dependency management.

## Pull Requests Merged
- **PR #1787**: Fixed Gentoo ebuild issues.
- **PR #1771**: Updated nativefiledialog to keep dialogs on top.
- **PR #1783**: Corrected a typo in CMakeLists.txt.

## File Changes
- **VERSION**: Bumped version to v1.35.4.
- **build.yml**: Updated the download link for Mesa3D.
- **CMake and Build Scripts**: Various modifications to improve build processes and dependency management.
- **Web Source Files**: Adjusted styles and scripts for better performance and user interaction.

This release brings significant improvements to the ImHex experience, particularly for Windows users and those using the web version. The updates to libraries and build processes ensure a more stable and efficient development environment.