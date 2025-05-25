# v4.8.0
## ✨ feat
- The latest update introduces the "-c-ldef" compression option for the hdiffz tool, utilizing the libdeflate compressor, compatible with zlib and offering improved speed or compression efficiency. Support for Android 15 with a 16KB page size has been added. The build process now includes a new flag for replacing the zlib decompressor with libdeflate, and the ldefDecompressPlugin has been introduced, significantly enhancing decompression speed. [#391](https://github.com/sisong/HDiffPatch/pull/391) 

## 📚 docs
- Documentation updated for compatibility with additional patch file formats. [619dcc7](https://github.com/sisong/HDiffPatch/commit/619dcc714a773f3faefd89c0bb532096f1037cb1)
