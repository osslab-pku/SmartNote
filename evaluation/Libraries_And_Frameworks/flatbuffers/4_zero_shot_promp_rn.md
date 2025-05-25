# Release Notes for v24.3.25

## Overview
This release includes several important updates and fixes, enhancing the functionality and compatibility of the FlatBuffers library. Key changes include improvements in handling string views, updates to license metadata, and adjustments to build configurations.

## New Features
- **Lobster Language Support**: Added support for required fields in Lobster, enhancing the language's capabilities for defining mandatory data structures.

## Bug Fixes
- **License Metadata**: Corrected the license string in `package.json` to improve compatibility with software license scanners. This ensures that the library's licensing information is accurately detected and reported (#8253).
- **String View Handling**: Fixed an issue with handling non-null-terminated `string_view` in `LookupByKey` function. This update allows `LookupByKey` to work correctly with `string_view` and other string-like objects, not just null-terminated C-style strings (#8203).

## Build and Configuration
- **Xcode Version**: Reverted the macOS build environment to use Xcode 14.2 due to compatibility issues with Xcode 14.3. This change ensures stable builds on macOS platforms.
- **Version Updates**: Updated version numbers across various files and configurations to reflect the new release version 24.3.25.

## Documentation
- **Changelog**: Updated the changelog to include the latest changes and improvements in this release.

## Contributors
- Wouter van Oortmerssen
- Thomas Hartwig
- Derek Bailey
- mpawlowski-eyeo

We appreciate the contributions from our community and encourage users to report any issues or suggestions for future improvements.