# 2.21.14
## 🐛 fix
- Updated FileViewport text mode to use UTF-8 encoding. [#524](https://github.com/Col-E/Recaf/pull/524) <span style='color:grey;'>(significance=0.37)</span>
- Resolved infinite loading on launch by modifying configuration directory path logic. [#756](https://github.com/Col-E/Recaf/pull/756) <span style='color:grey;'>(significance=0.33)</span>
- New translations and optimizations for existing translations in the zh-cn locale. [#587](https://github.com/Col-E/Recaf/pull/587) <span style='color:grey;'>(significance=0.20)</span>
- Fixed a typo in PRIMER.md, correcting "reccomended" to "recommended". [#557](https://github.com/Col-E/Recaf/pull/557) <span style='color:grey;'>(significance=0.15)</span>
- Introduced an "itf" suffix for invokestatic calls to handle static interface method invocations. Updated the disassembler, method instruction AST, and parser to support the new suffix. Added test cases to verify correct handling and suggestion of the "itf" suffix. [#591](https://github.com/Col-E/Recaf/pull/591) <span style='color:grey;'>(significance=0.13)</span>

## ✨ feat
- Enhanced mapping file dialog to support Jadx mapping files. [#516](https://github.com/Col-E/Recaf/pull/516) <span style='color:grey;'>(significance=0.21)</span>
- The auto-updater has been removed, and a notice added to inform users about the upcoming 4.X version. [e5669cd](https://github.com/Col-E/Recaf/commit/e5669cd90c7ea6e1a3851ff9065ee687cf7bdeb9) <span style='color:grey;'>(significance=0.18)</span>

## 🔧 chore
- Updated jsoup library from 1.14.3 to 1.15.3, including a security fix for potential XSS attacks, improved error message descriptions, and several bug fixes. [#599](https://github.com/Col-E/Recaf/pull/599) <span style='color:grey;'>(significance=0.15)</span>
- Fixed misspelling of "parameters" in some instruction parsers. [#757](https://github.com/Col-E/Recaf/pull/757) <span style='color:grey;'>(significance=0.16)</span>
- Minor cleanup in the codebase: modified `SourceCode.java` to improve node context checking logic and updated `IllegalBytecodePatcherUtil.java` to streamline bytecode patching by removing unnecessary comments and redundant code. [87695aa](https://github.com/Col-E/Recaf/commit/87695aac09a8407f99bbb37426b77b6c63f62bcc) <span style='color:grey;'>(significance=0.12)</span>

## 📚 docs
- A video explaining the current state and future plans of the Recaf developer space has been added to the README. [3877b1a](https://github.com/Col-E/Recaf/commit/3877b1a840b0fd8bfc4c3b655f5f9e080e621f65) <span style='color:grey;'>(significance=0.15)</span>