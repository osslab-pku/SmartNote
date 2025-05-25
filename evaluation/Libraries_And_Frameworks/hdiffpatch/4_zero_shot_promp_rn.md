# Release Notes for v4.8.0

## Overview
The v4.8.0 release introduces several enhancements and new features, particularly focusing on improved compression and decompression capabilities, support for new platforms, and various build system updates. This release also includes bug fixes and performance improvements.

## New Features
- **Libdeflate Integration**: 
  - Added support for the `-c-ldef` option in `hdiffz`, utilizing the libdeflate compressor. This option is compatible with `-c-zlib` and offers faster or better compression than zlib.
  - Introduced `ldefCompressPlugin`, `pldefCompressPlugin`, and `ldefDecompressPlugin` for enhanced compression and decompression performance.
  - Multi-threaded parallel support for the libdeflate compressor, improving speed and efficiency.

- **Android Support**:
  - Added support for Android 15 with a 16KB page size, ensuring compatibility with newer Android versions.

## Improvements
- **Decompression Speed**: 
  - The `ldefDecompressPlugin` now supports all deflate encodings, offering decompression speeds up to twice as fast as the zlib decompressor.
  - Improved handling of deflate code's last block end state for better performance.

- **Build System Enhancements**:
  - Updated build configurations for various platforms, including Code::Blocks, Xcode, and Visual Studio, ensuring successful builds across different environments.
  - Added new build options and configurations in the Makefile to support the integration of libdeflate and other libraries.

## Bug Fixes
- Fixed issues with the iOS SDK build and CI configurations to ensure stable and reliable builds.
- Resolved problems related to the recoding of test diff files and added a variable `isSingleCompressedBsDiff` for better control.

## Documentation
- Updated documentation to reflect new features and changes, including the addition of new command-line options and build instructions.
- Enhanced README files to provide clearer guidance on using the new features and configurations.

## Miscellaneous
- Updated the version number to v4.8.0 and made corresponding changes in the documentation and CI configurations.
- Various code refactoring and cleanup to improve code quality and maintainability.

For a detailed list of changes, please refer to the [full changelog](https://github.com/sisong/HDiffPatch/commits).