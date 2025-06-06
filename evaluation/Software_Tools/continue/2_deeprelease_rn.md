
## Features

- Ux improvements on control plane settings (#1924)
- Recursively apply quick actions codelens (#1925)
- Feature support model capability (#1810)
- .env ` .env ` (#1933)
- Fix failing test (#1903)
- Preview ` preview ` (#1930)
- .env ` .env ` (#1956)
- Preview ` preview ` (#1934)
- Preview ` preview ` (#1750)
- Moving bedrock integration to converse api to support all models (#1871)
- Implements watsonx model provider (#1831)
- More openai adapters (#1875)
- Query vllm openai /models endpoint to get model name and context window (#1632)

## BugFix

- Fix codestral name warning (#1914)
- Fix : filepath replacements in prompt files (#1939)
- Fixes paste bug (#1899)
- Fix : ts ignore declaration file issue w/ dbinfoz (#1945)
- Disable autocomplete in config.json (#1857)
- Copy-paste fix for ` code-server ` environments (#1844)
- Handle closed webview on quick edit (#1942)
- Change the ondidsavetextdocument handler to only reindex the single saved file (#1873)
- Fix codebaseindexer path path (#1870)
- Convert chunkcodebaseindexer 's sqlite inserts into a single bulk insert to improve performance (#1943)
- Update ` select-model.md ` (#1879)
- Fix vs code settings (#1882)
- Infopopup : infopopup (#1929)
- Change chunkcodebaseindex to add a tag for known chunks rather than rechunking the file (#1926)
- Fix error after sending an empty value to the voyage reranker api (#1902)
- Step control icons and layout adjustment (#1909)
- Fix tests (#1884)
- Fix : improve textarea ux (#1901)
- Update refreshindex.ts (#1866)
- Pre-release changes (#1927)
- Remove .prompts (#1883)
- Convert core/ to nodenext (#1877)
- Pre-release changes (#1928)
- Update prompt-files.md (#1940)
- Fix missing code snippets due to uncaught minisearch exception (#1796)

## Documentation

- Docs : add privacy section in docs sidebar (#1910)
- Updated azure open ai documentation (#1846)
- Add link to prompt library (#1922)
- Pre-release changes [ skip ci ] (#1931)
- Remove stale docs (#1897)
- Fix typo in slash commands docs (#1898)

## NonFunctional

- Configure docs through config.json (#1864)
- Enable async encoding for the gptencoder (#1946)
- Change the lancedbindex to compute its new cache rows in parallel and then do a bulk insert (#1944)
- Migrate walkdir from using minimatch to ignore.ignore for matching .gitignore patterns (#1880)
- Chore : bump target and lib versions for tsconfig (#1949)
- Enable sqlite wal ( write-ahead logging mode for improved concurrency (#1885)
- Update prompt files (#1867)
- Feat : improve input and tooltip ux (#1923)
- Make indexing functional in large workspaces by chunking segments of the workspace instead of the entire at once (#1876)
