# 1.2.0
## ✨ feat
- Settings now display device IP addresses. [1be5e28](https://github.com/getumbrel/umbrel/commit/1be5e28b329238899d49e77d5f175a7dcd118e55) 
- Added a GitHub action to manage translations: scans UI files to remove unused keys, checks for missing variables in non-English locales, removes non-English keys not in the English locale, generates missing translations, and sorts all locales. Translations in locale files are now sorted alphabetically. [d61acb9](https://github.com/getumbrel/umbrel/commit/d61acb9e25e266922cf37570d0f8918f44db34ce) [209baa9](https://github.com/getumbrel/umbrel/commit/209baa957688c1ba55de827f6507b9c94d1ce5a0) 

## 🐛 fix
- The latest software updates are now fetched automatically when the release channel changes. [ed1fe8f](https://github.com/getumbrel/umbrel/commit/ed1fe8fe2c8a9e4183502b52f6a8f95b3c466bd4) 
- Added missing Portuguese translation for "terminal" in the localization file. [0fc55ab](https://github.com/getumbrel/umbrel/commit/0fc55ab8a0bb3534a8489c109e1a34e251ade24e) 

## ♻️ refactor
- Removed console logs and improved code formatting. [7d3f6ac](https://github.com/getumbrel/umbrel/commit/7d3f6ac8aeb231f4a43a5882aca1ff7dae482b30) 

## 🔧 chore
- Finalized umbrelOS 1.2 release: updated version and version name in package.json, modified update script URLs to new release. Removed unused translations. [fc330d5](https://github.com/getumbrel/umbrel/commit/fc330d5ec62bc4a844695234e4802f32c3761a86) [d48c780](https://github.com/getumbrel/umbrel/commit/d48c780b9493daf04ab16e87caa7f077868f5f33)
