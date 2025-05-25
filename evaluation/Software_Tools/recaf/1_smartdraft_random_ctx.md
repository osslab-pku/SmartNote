# 2.21.14
## ✨ feat
- Introduces new translations and optimizes existing ones for the zh-cn locale. [#587](https://github.com/Col-E/Recaf/pull/587) 
- The auto-updater has been removed. Users are informed that version 4.X is the next intended version for migration. A notice about the upcoming Recaf 4.0.0 release has been added, highlighting new features and improvements. [e5669cd](https://github.com/Col-E/Recaf/commit/e5669cd90c7ea6e1a3851ff9065ee687cf7bdeb9) 

## 🐛 fix
- Added support for Jadx mapping files in the mapping file dialog. [#516](https://github.com/Col-E/Recaf/pull/516) 
- Updated FileViewport text mode to use UTF-8 encoding. [#524](https://github.com/Col-E/Recaf/pull/524) 
- Introduced an "itf" suffix to invokestatic calls to indicate interface method calls, as required by the JVM verifier. Modified the disassembler to append "itf" for interface methods and added a new ItfAST class to represent this suffix in the abstract syntax tree. Updated MethodInsnAST to handle the suffix and adjusted MethodInsnParser to parse and suggest it. Added tests to ensure correct parsing, printing, and suggestion of the "itf" suffix in invokestatic calls. [#591](https://github.com/Col-E/Recaf/pull/591) 
- Addresses an issue with application initialization logic on Windows. [#756](https://github.com/Col-E/Recaf/pull/756) 
- Corrected "parameters" misspelling in various instruction parsers. [#757](https://github.com/Col-E/Recaf/pull/757) 

## 🔧 chore
- Updated the jsoup library from 1.14.3 to 1.15.3, including a security fix for potential XSS attacks, improved error messages, and several bug fixes. [#599](https://github.com/Col-E/Recaf/pull/599) 
- Bumped the Guava library from 31.1-jre to 32.0.0-jre, including security fixes for CVE-2020-8908 and CVE-2023-2976 by reimplementing `Files.createTempDir` and `FileBackedOutputStream`. [#662](https://github.com/Col-E/Recaf/pull/662) 
- Minor cleanup in `SourceCode.java` and `IllegalBytecodePatcherUtil.java`, refactoring for better readability and maintainability. [87695aa](https://github.com/Col-E/Recaf/commit/87695aac09a8407f99bbb37426b77b6c63f62bcc) 

## 📚 docs
- Fixed a documentation typo. [#557](https://github.com/Col-E/Recaf/pull/557) 
- A video explaining the current state and future plans of the Recaf developer space has been added to the documentation. [3877b1a](https://github.com/Col-E/Recaf/commit/3877b1a840b0fd8bfc4c3b655f5f9e080e621f65)
