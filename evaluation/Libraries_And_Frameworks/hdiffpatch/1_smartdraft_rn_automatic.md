# v4.8.0
## ✨ feat
- The hdiffz project introduced a new compression option "-c-ldef" using the libdeflate compressor, compatible with zlib and offering improved speed or compression efficiency. The makefile includes a flag to replace the zlib decompressor with libdeflate for certain operations. The ldefDecompressPlugin enhances decompression speed. The Android library now supports Android 15 with a 16KB page size. [#391](https://github.com/sisong/HDiffPatch/pull/391) <span style='color:grey;'>(significance=0.64)</span>

## 📚 docs
- Documentation updated to clarify compatibility with bsdiff4, endsley/bsdiff, open-vcdiff, and xdelta3 formats. README files and usage instructions in the code now reflect these changes. [619dcc7](https://github.com/sisong/HDiffPatch/commit/619dcc714a773f3faefd89c0bb532096f1037cb1) <span style='color:grey;'>(significance=0.22)</span>