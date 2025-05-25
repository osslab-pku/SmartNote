# 8.1.0

## 🛠️ Breaking Changes & Security
- Addresses an issue where tables could be suspended under memory pressure. Introduces mechanisms to manage memory pressure more effectively, including adjustments to sleep intervals and error handling to prevent table suspension. Adds new methods and classes to track and regulate memory usage, ensuring smooth operations even when memory is constrained. Enhances system resilience and stability under high memory usage scenarios. [#4745](https://github.com/questdb/questdb/pull/4745) 
 <span style='color:grey;'>(significance=0.11)</span>

## 🐛 fix
- The update fixes "unsupported operation" errors in SQL queries, improving handling of null values, type mismatches, and invalid arguments. Enhanced error messages for clarity and debugging. New test cases validate these fixes for robust functionality. [#4632](https://github.com/questdb/questdb/pull/4632) 
 <span style='color:grey;'>(significance=0.25)</span>
- Fixed incorrect results from parallel WHERE and GROUP BY operations for certain function keys by ensuring thread safety and correct handling of string sinks. [#4796](https://github.com/questdb/questdb/pull/4796) 
 <span style='color:grey;'>(significance=0.15)</span>
- Fixed an issue with window functions double counting rows by modifying `CachedWindowRecordCursorFactory` to build the record chain only once. Added a test case to `WindowFunctionTest` to verify correct behavior when ordered by a non-timestamp column with a negative limit. [#4804](https://github.com/questdb/questdb/pull/4804) 
 <span style='color:grey;'>(significance=0.17)</span>
- Fixed incorrect results from parallel GROUP BY queries with a single varchar function key. [#4798](https://github.com/questdb/questdb/pull/4798) 
 <span style='color:grey;'>(significance=0.10)</span>

## 🚀 perf
- Improved performance of `like` and `ilike` operators on symbol columns. Enhanced expression parsing and SQL code generation, introduced new function factories for handling these operations. Added and updated test cases to ensure correctness and efficiency. [#4794](https://github.com/questdb/questdb/pull/4794) 
 <span style='color:grey;'>(significance=0.11)</span>
- Improved `regexp_replace(varchar)` performance for simple patterns by skipping UTF-8 decoding for ASCII-only patterns, resulting in faster execution. Added tests to ensure optimization correctness. [#4668](https://github.com/questdb/questdb/pull/4668) 
 <span style='color:grey;'>(significance=0.14)</span>

## 🧪 test
- Re-enabled the deduplication insert fuzz test. [#4780](https://github.com/questdb/questdb/pull/4780) 
 <span style='color:grey;'>(significance=0.12)</span>

## 👷 ci
- Added support for building Docker images with Red Hat Universal Base Image (UBI). [#4783](https://github.com/questdb/questdb/pull/4783) 
 <span style='color:grey;'>(significance=0.18)</span>
- Fixed the build process for the RHEL Docker image. [#4791](https://github.com/questdb/questdb/pull/4791) 
 <span style='color:grey;'>(significance=0.17)</span>

## 🔧 chore
- Hid the pre-touch magic number shutdown message in system logs. The magic number, used to prevent JVM's JIT compiler from optimizing away certain instructions, is now logged at the debug level instead of standard error output. [#4767](https://github.com/questdb/questdb/pull/4767) 
 <span style='color:grey;'>(significance=0.11)</span>