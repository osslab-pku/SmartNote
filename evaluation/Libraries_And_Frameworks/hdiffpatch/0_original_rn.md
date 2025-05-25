[CHANGE LOG ...](https://github.com/sisong/HDiffPatch/blob/master/CHANGELOG.md)    
   
Note:    
* create a delta: `$hdiffz -m-6 -SD -c-zstd-21-24 -d oldPath newPath outDiffFile` ; if file is very large, try changing `-m-6` to `-s-64`; apply the delta: `$hpatchz oldPath diffFile outNewPath`
* I did not tested linux_riscv32 cmdline on riscv linux PC
* I did not tested windows_arm32 & windows_arm64 cmdline on Arm Windows PC
* libhpatchz.so in `android_hpatchz/libs` support decompressor: zlib,lzma,lzma2,zstd , & support diffFile created by $hdiffz,$hdiffz -SD
* libhpatchz.so in `android_hpatchz/libs_patchers` support decompressor: zlib,lzma,lzma2,zstd,bzip2 , & support diffFile created by $hdiffz,$hdiffz -SD,$hdiffz -BSD,$bsdiff4,$hdiffz -VCD,$open-vcdiff delta,$xdelta3 -S,$xdelta3 -S lzma
* libhpatchz.a in `ios_macos_hpatchz` support iOS,macos , & support decompressor: zlib,lzma,lzma2,zstd,bzip2 , & support diffFile created by $hdiffz,$hdiffz -SD,$hdiffz -BSD,$bsdiff4,$hdiffz -VCD,$open-vcdiff delta,$xdelta3 -S,$xdelta3 -S lzma