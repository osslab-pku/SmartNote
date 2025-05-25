# v24.3.25
## ✨ feat
- Added support for required fields, enhancing field requirements handling in code generation. [960cd4d](https://github.com/google/flatbuffers/commit/960cd4d635b98fc5daeeafee8b0a5601d45c70ad)
- Fixed handling of non-null-terminated string_views in LookupByKey. Overloaded KeyCompareWithValue function for string-like objects to ensure proper comparison and lookup. Added tests to verify correctness. Enhanced the C++ library to allow `string_view` in `LookUpByKey` alongside null-terminated C-style strings. [#8203](https://github.com/google/flatbuffers/pull/8203) [595bf00](https://github.com/google/flatbuffers/commit/595bf0007ab1929570c7671f091313c8fc20644e)

## 🐛 fix
- Updated the license value in package.json to "Apache-2.0" for compatibility with most software license scanners. [#8253](https://github.com/google/flatbuffers/pull/8253)

## 🔧 chore
- Updated macOS build configuration to use Xcode 14.2 due to issues with Xcode 14.3. [67eb95d](https://github.com/google/flatbuffers/commit/67eb95de9281087ccbba9aafd6e8ab1958d12045)
