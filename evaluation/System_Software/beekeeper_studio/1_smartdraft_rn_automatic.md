# v4.6.2

## 🛠️ Breaking Changes & Security
- The launcher script now defaults to --no-sandbox due to distros disabling clone for non-root users, ensuring smoother operation. Updated .gitignore to include *.db files. [89c59c3](https://github.com/beekeeper-studio/beekeeper-studio/commit/89c59c3303107029d28a6888676dabd6608952c3) 
 <span style='color:grey;'>(significance=0.17)</span>

## ✨ feat
- A special table for supported databases has been added, with one page dedicated to each. The connection screen documentation now includes a detailed table of supported databases and their support levels. The SQLite documentation includes information on file associations for .db and .sqlite3 files. The mkdocs.yml configuration file has been updated to reorganize the navigation structure, adding new sections for connecting to and supporting databases. [#2262](https://github.com/beekeeper-studio/beekeeper-studio/pull/2262) 
 <span style='color:grey;'>(significance=0.10)</span>

## ♻️ refactor
- Users can now reopen the last closed tab using the 'Ctrl+Shift+T' shortcut. The tab management system restores tabs to their correct positions with a new `position` attribute in the tab model. Refactored logic for handling last closed tabs is now in the tab module, simplifying tracking. The system maintains a stack of closed tabs, allowing users to reopen multiple tabs. [#1963](https://github.com/beekeeper-studio/beekeeper-studio/pull/1963) 
 <span style='color:grey;'>(significance=0.15)</span>

## 🔧 chore
- Implemented bug fixes to improve the update-readmes job in the workflow. Updated workflow for README file updates and supported databases documentation. Streamlined file content updates with additional status checks before committing changes. Adjusted supported databases documentation for formatting consistency. [b60693c](https://github.com/beekeeper-studio/beekeeper-studio/commit/b60693cde3e6fcaead508460f957d3e9ce37da1d) [22b8865](https://github.com/beekeeper-studio/beekeeper-studio/commit/22b8865e659901294e74799e9fa6f1e288bf0ac9) 
 (significance=0.16, 0.13)