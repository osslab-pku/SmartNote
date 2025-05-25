# 2.21.14
## ✨ feat
- Added support for Jadx mapping files in the mapping file dialog. [#516](https://github.com/Col-E/Recaf/pull/516) <span style='color:grey;'>(significance=0.27)</span>
- The update removes the auto-updater feature and introduces a notification about the upcoming major version 4.X, encouraging users to migrate. [e5669cd](https://github.com/Col-E/Recaf/commit/e5669cd90c7ea6e1a3851ff9065ee687cf7bdeb9) <span style='color:grey;'>(significance=0.18)</span>
## 🐛 fix
- The pull request fixes an encoding issue in FileViewport's text mode by switching from the system's default charset to UTF-8, ensuring correct text display for Java developers. [#524](https://github.com/Col-E/Recaf/pull/524) <span style='color:grey;'>(significance=0.41)</span>
- Corrected a typo in the documentation for clarity. [#557](https://github.com/Col-E/Recaf/pull/557) <span style='color:grey;'>(significance=0.22)</span>
- The pull request adds an "itf" suffix to invokestatic calls for correct interface method reference handling, required by the JVM verifier. This change includes updates to the disassembler, parser, and abstract syntax tree structure. [#591](https://github.com/Col-E/Recaf/pull/591) <span style='color:grey;'>(significance=0.19)</span>
- The update fixes infinite loading on launch by modifying the configuration directory initialization process. [#756](https://github.com/Col-E/Recaf/pull/756) <span style='color:grey;'>(significance=0.41)</span>
## 🔧 chore
- Added new Chinese translations and optimized existing ones to enhance the user interface and experience. [#587](https://github.com/Col-E/Recaf/pull/587) <span style='color:grey;'>(significance=0.24)</span>
- Updated the jsoup library to address an XSS vulnerability, improve error message descriptions, and fix bugs. [#599](https://github.com/Col-E/Recaf/pull/599) <span style='color:grey;'>(significance=0.17)</span>
- Corrected the misspelling of "parameters" in various instruction parsers. [#757](https://github.com/Col-E/Recaf/pull/757) <span style='color:grey;'>(significance=0.23)</span>
- Minor codebase cleanup improves node context retrieval logic and refines the bytecode patching utility. Enhances code clarity and efficiency by restructuring conditional statements and removing unnecessary comments and code segments. [87695aa](https://github.com/Col-E/Recaf/commit/87695aac09a8407f99bbb37426b77b6c63f62bcc) <span style='color:grey;'>(significance=0.12)</span>
## 📚 docs
- A video explains developments in the Recaf developer space, including future plans. [3877b1a](https://github.com/Col-E/Recaf/commit/3877b1a840b0fd8bfc4c3b655f5f9e080e621f65) <span style='color:grey;'>(significance=0.17)</span>
