QuestDB 8.1.0 has arrived. 

In this release, QuestDB's foundation takes a second step towards our next generation architecture. 

Our prior release introduced JSON extraction.

And now, by popular demand, QuestDB meets Apache Parquet.

### New Features 🐣

- **Parquet read support** Use the `read_parquet()` function to read [Apache Parquet](https://questdb.io/glossary/apache-parquet) files.
- **Improved SAMPLE BY:**
  - FROM-TO syntax: Specify result ranges, with support for prefilling and postfilling data. Also can correct misaligned buckets.
  - Parallel SAMPLE BY: Now supports `FILL(VALUE)` and `FILL(NULL)`.
- **Snapshot recovery:** Added a trigger file to initiate snapshot recovery, improving database resilience and ease-of-use.

### Performance 🚀

- **Improved ILP ingress latency**
- **SQL Performance:**
  - Speedup for small transaction writing by 50-100%.
  - Enhanced performance for the `like/ilike` operator on symbol columns.
  - Speed improvements for `regexp_replace(varchar)` with simple patterns.
- **Aggregation queries:** Aggregation queries are now faster. 

### Bug Fixes 🐛

- **SQL:**
  - Fixed spurious "unsupported operation" errors.
  - Corrected wrong results from parallel `WHERE` and `GROUP BY` for some function keys.
  - Fixed incorrect results from parallel `GROUP BY` with a single varchar function key.
  - Addressed issues with some window functions double counting rows.

- **Core:**
  - Prevented table suspension under memory pressure.
  - Fixed Charts when using together with OAuth.

## Pull requests

* fix(sql): fix spurious "unsupported operation" errors by @bluestreak01 in https://github.com/questdb/questdb/pull/4632
* perf(core): speedup small transaction writing 50-100% by @ideoma in https://github.com/questdb/questdb/pull/4793
* fix(sql): fix wrong results returned from parallel WHERE and GROUP BY for some function keys by @puzpuzpuz in https://github.com/questdb/questdb/pull/4796
* fix(sql): incorrect results returned from parallel GROUP BY with single varchar function key by @puzpuzpuz in https://github.com/questdb/questdb/pull/4798
* fix(core): avoid table suspension when under memory pressure by @jerrinot in https://github.com/questdb/questdb/pull/4745
* perf(sql): speed up like/ilike operator on symbol column by @puzpuzpuz in https://github.com/questdb/questdb/pull/4794
* perf(sql): speed up regexp_replace(varchar) for simple patterns by @puzpuzpuz in https://github.com/questdb/questdb/pull/4668
* fix(sql): some window functions might double count rows by @jerrinot in https://github.com/questdb/questdb/pull/4804
* feat(sql): read_parquet() function by @eugenels in https://github.com/questdb/questdb/pull/4460
* feat(sql): introduce SAMPLE BY FROM-TO syntax for specifying result ranges by @nwoolmer in https://github.com/questdb/questdb/pull/4733
* fix(ui): fix Charts when using together with OAuth by @insmac in https://github.com/questdb/questdb/pull/4813
* feat(core): trigger file to initiate snapshot recovery by @jerrinot in https://github.com/questdb/questdb/pull/4807

## New Contributors
* @jchrys made their first contribution in https://github.com/questdb/questdb/pull/4808

**Full Changelog**: https://github.com/questdb/questdb/compare/8.0.3...8.1.0