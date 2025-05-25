# 8.1.0
## ✨ feat
- Enhanced SQL syntax with `SAMPLE BY FROM-TO` for precise result ranges, enabling better time interval definitions in queries. [#4733](https://github.com/questdb/questdb/pull/4733) <span style='color:grey;'>(significance=0.06)</span>
- Added feature to initiate snapshot recovery using a trigger file. Enhancements ensure robust handling of failure scenarios, with improved error handling and logging for file operations. New tests verify correct behavior of the snapshot recovery process under different conditions. [#4807](https://github.com/questdb/questdb/pull/4807) <span style='color:grey;'>(significance=0.06)</span>

## 🐛 fix
- Fixed "unsupported operation" errors in SQL queries, improving handling of edge cases and invalid inputs. Introduced new tests to verify these fixes, enhancing the robustness and reliability of the SQL engine. [#4632](https://github.com/questdb/questdb/pull/4632) <span style='color:grey;'>(significance=0.06)</span>
- Fixed incorrect results for parallel WHERE and GROUP BY queries with certain function keys. [#4796](https://github.com/questdb/questdb/pull/4796) <span style='color:grey;'>(significance=0.10)</span>
- Fixed an issue where certain SQL window functions could double count rows by ensuring the record chain is built only once during size calculation. Added a test to verify window functions with a negative limit when ordered by a non-timestamp column. [#4804](https://github.com/questdb/questdb/pull/4804) <span style='color:grey;'>(significance=0.05)</span>

## 🚀 perf
- Improved performance of `like` and `ilike` operators on symbol columns. [#4794](https://github.com/questdb/questdb/pull/4794) <span style='color:grey;'>(significance=0.06)</span>

## 🔧 chore
- The pre-touch magic number shutdown message is now hidden to prevent unnecessary log entries during shutdown, while maintaining JVM's JIT compiler optimization functionality. [#4767](https://github.com/questdb/questdb/pull/4767) <span style='color:grey;'>(significance=0.06)</span>
- The commit fixes the sqllogictest binary load for proper functionality when QuestDB is a submodule. It adds a README for the Rust JNI bindings project with build and usage instructions. Modifications in TestOs.java ensure correct binary file location and loading based on last modified times. [#4809](https://github.com/questdb/questdb/pull/4809) <span style='color:grey;'>(significance=0.08)</span>