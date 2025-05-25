# v24.3.25
## ✨ feat
- Added support for required fields. [960cd4d](https://github.com/google/flatbuffers/commit/960cd4d635b98fc5daeeafee8b0a5601d45c70ad) <span style='color:grey;'>(significance=0.05)</span>
- Enhanced the C++ library to allow `string_view` in `LookUpByKey` alongside null-terminated C-style strings. [595bf00](https://github.com/google/flatbuffers/commit/595bf0007ab1929570c7671f091313c8fc20644e) <span style='color:grey;'>(significance=0.01)</span>

## 🐛 fix
- Fixed handling of non-null-terminated `string_view` in `LookUpByKey`. Overloaded `KeyCompareWithValue` function for string-like objects to ensure proper comparison. Added tests to verify correctness. [#8203](https://github.com/google/flatbuffers/pull/8203) <span style='color:grey;'>(significance=0.06)</span>
- Updated the license value to "Apache-2.0" for compatibility with most software license scanners. [#8253](https://github.com/google/flatbuffers/pull/8253) <span style='color:grey;'>(significance=0.03)</span>

## 🔧 chore
- Updated macOS build configuration to use xcode 14.2 due to issues with xcode 14.3. [67eb95d](https://github.com/google/flatbuffers/commit/67eb95de9281087ccbba9aafd6e8ab1958d12045) <span style='color:grey;'>(significance=0.03)</span>