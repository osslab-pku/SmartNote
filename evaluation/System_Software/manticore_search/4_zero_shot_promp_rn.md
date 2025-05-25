# Release Notes for Version 6.3.4

## Release Date
July 31, 2024

## Overview
Version 6.3.4 is a minor release that focuses on bug fixes and minor improvements to enhance the stability and performance of the system. This release includes updates to dependencies, improvements in query handling, and several bug fixes.

## Key Changes

### Bug Fixes
- **Join Operations**: Fixed issues with join filters on columnar attributes from the right table when the attribute is not in the select list. Also addressed left join returning non-matching entries when `match()` over the right table is used.
- **Aggregation and Sorting**: Resolved a crash on MVA min or max for empty MVA arrays and fixed range aggregation result sets for infinite range cases.
- **Query Handling**: Fixed errors related to full-text vs filter order in JSON queries and improved handling of presort/prefilter expressions that depend on joined attributes.
- **Indexing and Storage**: Fixed the save of disk chunks at RT index with `hitless_words` and disabled local_df calculation for all wildcard terms in queries to improve performance.
- **Build and Compatibility**: Fixed `xxhash` build issues on Visual Studio and GCC, and updated the build process for better compatibility.

### Improvements
- **Documentation**: Added integration information for DBeaver, a popular SQL client, to facilitate easier database management.
- **Configuration**: Set a new default for `max_packet_size` to 128Mb to ensure all CI tests pass smoothly.
- **Dependency Updates**: Updated several dependencies including `executor`, `buddy`, and `mcl` to their latest versions for improved performance and security.
- **CI Enhancements**: Improved CI processes, including better handling of Docker tags and enhancements in the test kit build scripts.

### New Features
- **Secondary Indexes**: Implemented secondary indexes for JSON attributes, including support for `IS NULL`/`IS NOT NULL` filters.
- **Content-Encoding Support**: Added support for `content-encoding:gzip` for all HTTP requests to optimize data transfer.

## Detailed Changes

### Pull Requests Merged
- **PR #2455**: Updated `Low-level_tokenization.md` to fix a typo.
- **PR #2456**: Addressed binlog-related issues.
- **PR #2316**: Removed fake nested aggs support in the HTTP search endpoint.
- **PR #2359**: Fixed renaming of external files on alter and create table operations.
- **PR #2434**: Set new default for `max_packet_size`.
- **PR #2443**: Fixed `xxhash` build on GCC.
- **PR #2459**: Improved GitHub CI build and test processes.
- **PR #2450**: Updated `mcl` version to 2.3.1.
- **PR #2457**: Updated `buddy` version to 2.3.13.
- **PR #2453**: Fixed miscellaneous JSON SI related issues.
- **PR #2451**: Updated supported versions in the mysqldump supported versions test.
- **PR #2445**: Updated `buddy` version to 2.3.13.
- **PR #2440**: Added support for `content-encoding:gzip` for all HTTP requests.
- **PR #2428**: Added test for `CREATE TABLE new_table LIKE existing_table`.
- **PR #2421**: Updated `buddy` version to 2.3.13.
- **PR #2433**: Fixed allocation of the `max_packet_size` buffer for the initial socket probe.
- **PR #2424**: Fixed issues with `manticore_new_cluster`.
- **PR #2416**: Fixed KNN queries vs distributed tables.
- **PR #2413**: Fixed `total_relation` vs multiquery with cutoff.
- **PR #2412**: Fixed `SHOW CREATE TABLE` vs SI and SI filter transforms when SI is unavailable.
- **PR #2409**: Updated `buddy` version to 2.3.13.
- **PR #2390**: Introduced per-index binlog feature.
- **PR #2408**: Updated `buddy` version to 2.3.13.
- **PR #2394**: Updated `backup` version to 1.3.9.
- **PR #2399**: Fixed filtering by `json.string` in the right table on table join.
- **PR #2397**: Fixed a crash on fetching attribute dependencies at result set merge.
- **PR #2391**: Updated integration tests to pass with the updated version.
- **PR #2388**: Updated `buddy` version to 2.3.13.
- **PR #2386**: Added support for JSON objects in `IS NULL` filters.
- **PR #2387**: Updated `buddy` version to 2.3.13.
- **PR #2383**: Updated test-supported-mysqldump-versions.rec for mysqldump 9 support.
- **PR #2382**: Fixed JSON SI vs `IN()` filters and filter include/exclude handling.
- **PR #2378**: Updated `buddy` version to 2.3.13.
- **PR #2371**: Changed JSON field name to SI name conversion.
- **PR #2330**: Created integration tests, separated logstash and filebeat tests.
- **PR #2360**: Updated CLT tests due to RHEL 7 EOL.
- **PR #2358**: Updated test-character-transformation-when-sending-to-buddy.rec.
- **PR #2357**: Updated `mcl` version to 2.3.1.
- **PR #2353**: Added `IS NULL`/`IS NOT NULL` filter support to secondary indexes for JSON attributes.
- **PR #2310**: Implemented secondary indexes for JSON attributes.
- **PR #2336**: Created test-integrations-filebeat.rec.
- **PR #2345**: Fixed left join returning non-matching entries when `match()` over the right table is used.
- **PR #2341**: Fixed join filter on columnar attributes from the right table when the attribute is not in the select list.
- **PR #2340**: Updated rhel-release-install.rec for correct package deletion.
- **PR #2334**: Fixed join on filter with two JSON attributes.

### File Changes
- **CMake and Build Scripts**: Updated `GetxxHash.cmake` and build scripts for better compatibility and dependency management.
- **Documentation**: Added and updated documentation files, including integration guides and changelogs.
- **Source Code**: Various fixes and improvements in source files related to query processing, aggregation, and indexing.
- **Test Cases**: Added and updated test cases to cover new features and bug fixes.

This release ensures improved stability and performance, addressing several critical issues and enhancing the overall functionality of the system. Users are encouraged to update to this version to benefit from these improvements.