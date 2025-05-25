# v24.3.25
## ✨ feat
- Added support for required fields. [960cd4d](https://github.com/google/flatbuffers/commit/960cd4d635b98fc5daeeafee8b0a5601d45c70ad) <span style='color:grey;'>(significance=0.19)</span>
- Fixed handling of non-null-terminated string_views in LookUpByKey. Overloaded KeyCompareWithValue function for string-like objects to ensure proper comparisons. Added tests to verify functionality. Enhanced the C++ library to allow `string_view` in `LookUpByKey` alongside null-terminated C-style strings. [#8203](https://github.com/google/flatbuffers/pull/8203) [595bf00](https://github.com/google/flatbuffers/commit/595bf0007ab1929570c7671f091313c8fc20644e) (significance=0.26, 0.21)

## 🐛 fix
- Updated the license value in the package.json file to "Apache-2.0" for compatibility with most software license scanners. [#8253](https://github.com/google/flatbuffers/pull/8253) <span style='color:grey;'>(significance=0.09)</span>

## 🔧 chore
- Adjusted macOS build configuration to use Xcode 14.2 due to issues with Xcode 14.3. [67eb95d](https://github.com/google/flatbuffers/commit/67eb95de9281087ccbba9aafd6e8ab1958d12045) <span style='color:grey;'>(significance=0.14)</span>