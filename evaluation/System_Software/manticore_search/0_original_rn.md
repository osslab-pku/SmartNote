# Version 6.3.4
Released: July 31st 2024

➡️ [INSTALL](https://manticoresearch.com/install/) ⬅️

Version 6.3.4 continues the 6.3 series and includes only minor improvements and bug fixes.

### Minor changes
* [Issue #1130](https://github.com/manticoresoftware/manticoresearch/issues/1130) Added support for [DBeaver](https://manual.manticoresearch.com/Integration/DBeaver#Integration-with-DBeaver).
* [Issue #2146](https://github.com/manticoresoftware/manticoresearch/issues/2146) Improved escaping of delimiters in word forms and exceptions.
* [Issue #2268](https://github.com/manticoresoftware/manticoresearch/issues/2268) Improved external files renaming on copy for CREATE and ALTER TABLE statements.
* [Issue #2315](https://github.com/manticoresoftware/manticoresearch/issues/2315) Added string comparison operators to SELECT list expressions.
* [Issue #2363](https://github.com/manticoresoftware/manticoresearch/issues/2363) Added support for null values in Elastic-like bulk requests.
* [Issue #2374](https://github.com/manticoresoftware/manticoresearch/issues/2374) Added support for mysqldump version 9.
* [Issue #2375](https://github.com/manticoresoftware/manticoresearch/issues/2375) Improved error handling in HTTP JSON queries with JSON path to the node where the error occurs.

### Bug fixes
* [Issue #2280](https://github.com/manticoresoftware/manticoresearch/issues/2280) Fixed performance degradation in wildcard queries with many matches when disk_chunks > 1.
* [Issue #2332](https://github.com/manticoresoftware/manticoresearch/issues/2332) Fixed crash in MVA MIN or MAX SELECT list expressions for empty MVA arrays.
* [Issue #2339](https://github.com/manticoresoftware/manticoresearch/issues/2339) Fixed incorrect processing of Kibana's infinite range request.
* [Issue #2342](https://github.com/manticoresoftware/manticoresearch/issues/2342) Fixed join filter on columnar attributes from the right table when the attribute is not in the SELECT list.
* [Issue #2343](https://github.com/manticoresoftware/manticoresearch/issues/2343) Fixed duplicate 'static' specifier in Manticore 6.3.2.
* [Issue #2344](https://github.com/manticoresoftware/manticoresearch/issues/2344) Fixed LEFT JOIN returning non-matching entries when MATCH() over the right table is used.
* [Issue #2350](https://github.com/manticoresoftware/manticoresearch/issues/2350) Fixed saving of disk chunk at RT index with `hitless_words`.
* [Issue #2364](https://github.com/manticoresoftware/manticoresearch/issues/2364) The 'aggs_node_sort' property can now be added in any order among other properties.
* [Issue #2368](https://github.com/manticoresoftware/manticoresearch/issues/2368) Fixed error on full-text vs filter order in the JSON query.
* [Issue #2376](https://github.com/manticoresoftware/manticoresearch/issues/2376) Fixed bug related to incorrect JSON response for long UTF-8 requests.
* [Issue #2684](https://github.com/manticoresoftware/dev/issues/2684) Fixed calculation of presort/prefilter expressions that depend on joined attributes.
* [Issue #301](https://github.com/manticoresoftware/manticoresearch-buddy/issues/301) Changed the method of calculating data size for metrics to read from the `manticore.json` file instead of checking the entire size of the data directory.
* [Issue #302](https://github.com/manticoresoftware/manticoresearch-buddy/issues/302) Added handling of validation requests from Vector.dev.