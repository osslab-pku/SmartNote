# 8.1.0
## 🐛 fix
- Fixed incorrect results for parallel WHERE and GROUP BY queries with certain function keys. [#4796](https://github.com/questdb/questdb/pull/4796)
- Addressed an issue where tables could be suspended under memory pressure. Introduced mechanisms to manage memory pressure more effectively, preventing unnecessary table suspensions. Adjustments include sleep intervals, error handling improvements, and a parallelism regulator to control concurrent operations based on memory availability. Added new tests to ensure robustness under various conditions. [#4745](https://github.com/questdb/questdb/pull/4745)
- Fixed an issue where some SQL window functions double counted rows. [#4804](https://github.com/questdb/questdb/pull/4804)
- Fixed "unsupported operation" errors in SQL queries, ensuring functions and operations handle edge cases and invalid inputs more gracefully. Error messages are now more informative and user-friendly. Extensive testing verifies the correctness of these fixes and prevents regressions. [#4632](https://github.com/questdb/questdb/pull/4632)

## 🚀 perf
- Improved performance of `like` and `ilike` operators on symbol columns. [#4794](https://github.com/questdb/questdb/pull/4794)
- Optimized `regexp_replace(varchar)` for simple patterns, enhancing performance by avoiding UTF-8 decoding for ASCII-only patterns. [#4668](https://github.com/questdb/questdb/pull/4668)

## 👷 ci
- Added Docker build configuration to support Red Hat UBI, enhancing build process flexibility and compatibility. [#4783](https://github.com/questdb/questdb/pull/4783)
- Fixed the RHEL Docker image build process for compatibility with amd64 and arm64 platforms. [#4791](https://github.com/questdb/questdb/pull/4791)

## 🧪 test
- Re-enabled the dedup insert fuzz test. [#4780](https://github.com/questdb/questdb/pull/4780)

## 🔧 chore
- The pre-touch magic number shutdown message is now hidden from logs during the shutdown process. [#4767](https://github.com/questdb/questdb/pull/4767)
