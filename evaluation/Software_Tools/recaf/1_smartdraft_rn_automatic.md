# 2.21.14
## ✨ feat
- Added new and optimized existing Chinese translations. [#587](https://github.com/Col-E/Recaf/pull/587) <span style='color:grey;'>(significance=0.35)</span>
- The auto-updater has been removed. A notice informs users about the upcoming 4.X version, encouraging migration. [e5669cd](https://github.com/Col-E/Recaf/commit/e5669cd90c7ea6e1a3851ff9065ee687cf7bdeb9) <span style='color:grey;'>(significance=0.31)</span>

## 🐛 fix
- Introduced an "itf" suffix to invokestatic calls to indicate interface method calls, as required by the JVM verifier. Updated the disassembler, AST structures, and parsers to support this suffix. Added tests and suggestions for the "itf" suffix in relevant contexts. [#591](https://github.com/Col-E/Recaf/pull/591) <span style='color:grey;'>(significance=0.57)</span>
- Modified logic for determining the configuration directory path to prevent an infinite spin. Ensures the correct path is set based on the operating system, with specific handling for Windows. [#756](https://github.com/Col-E/Recaf/pull/756) <span style='color:grey;'>(significance=0.51)</span>
- Updated FileViewport text mode to use UTF-8 encoding, addressing encoding issues for Java developers. [#524](https://github.com/Col-E/Recaf/pull/524) <span style='color:grey;'>(significance=0.50)</span>
- Added support for Jadx mapping files in the mapping file dialog. [#516](https://github.com/Col-E/Recaf/pull/516) <span style='color:grey;'>(significance=0.31)</span>
- Fixed misspelling of "parameters" in instruction parsers. [#757](https://github.com/Col-E/Recaf/pull/757) <span style='color:grey;'>(significance=0.41)</span>

## 🔧 chore
- Bumped jsoup from 1.14.3 to 1.15.3, including a security fix for potential XSS attacks, more descriptive validation error messages, and other bug fixes and improvements. [#599](https://github.com/Col-E/Recaf/pull/599) <span style='color:grey;'>(significance=0.17)</span>
- Bumps com.google.guava:guava from 31.1-jre to 32.0.0-jre. Addresses security vulnerabilities CVE-2020-8908 and CVE-2023-2976 by reimplementing Files.createTempDir and FileBackedOutputStream. New implementations may cause issues for Windows users, resolved in version 32.0.1. guava-gwt now requires GWT 2.10.0, and there is a binary-incompatible change to a @Beta API in guava-testlib. [#662](https://github.com/Col-E/Recaf/pull/662) <span style='color:grey;'>(significance=0.22)</span>
- Minor codebase cleanup, including refactoring and improved readability of `SourceCode.java` and `IllegalBytecodePatcherUtil.java`. [87695aa](https://github.com/Col-E/Recaf/commit/87695aac09a8407f99bbb37426b77b6c63f62bcc) <span style='color:grey;'>(significance=0.42)</span>

## 📚 docs
- Fixed a typo in PRIMER.md, correcting "reccomended" to "recommended". [#557](https://github.com/Col-E/Recaf/pull/557) <span style='color:grey;'>(significance=0.28)</span>
- A video has been added to the README explaining the current state and future plans for the Recaf developer space, addressing versions 3X and 4X. [3877b1a](https://github.com/Col-E/Recaf/commit/3877b1a840b0fd8bfc4c3b655f5f9e080e621f65) <span style='color:grey;'>(significance=0.26)</span>