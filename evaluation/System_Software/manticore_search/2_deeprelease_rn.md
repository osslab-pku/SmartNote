
## Features

- Per-index binlog (#2390)
- Added support for content-encoding : gzip for all http requests (#2440)

## BugFix

- Test/create table like existing table with data (#2428)
- Set new default for max_packet_size to 128mb (#2434)
- Fixed a crash on fetching attr dependencies at rset merge (#2397)
- Update ` low-level_tokenization.md ` (#2455)
- Fixed show create table vs si ; fixed si filter transforms when si is unavailable (#2412)
- Fixed xxhash build on gcc (#2443)
- Fixed allocation of the max_packet_size buffer for the initial socket probe (#2433)
- Fixed filtering by json.string in right table on table join (#2399)
- Fixed total_relation vs multiquery with cutoff (#2413)

## Documentation

- Update backup version (#2394)
- Manticore_new_cluster broken ( pr ) (#2424)
- Fixed knn queries vs distributed tables (#2416)
- Update buddy version (#2464)
- Update mcl version (#2450)
- Update buddy version (#2421)
- Changing supported versions (#2451)
- Win zlib (#2459)
- Update buddy version (#2409)
- Fixed misc json si related issues (#2453)
- Update buddy version (#2408)
- Update buddy version (#2457)
- Update buddy version (#2445)
- Update buddy version (#2388)

## NonFunctional

- Update integrations tests (#2391)
- Fix binlog corruption on startup (#2456)
- Junk pr for ci pass (#2499)
- Tests : add clt tests for replace escaping (#2465)
