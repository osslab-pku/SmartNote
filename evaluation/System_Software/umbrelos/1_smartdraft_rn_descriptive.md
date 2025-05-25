# 1.2.0

## 🐛 fix
- The update fetches the latest software update whenever the release channel changes. [ed1fe8f](https://github.com/getumbrel/umbrel/commit/ed1fe8fe2c8a9e4183502b52f6a8f95b3c466bd4) <span style='color:grey;'>(significance=0.03)</span>
- Added missing Portuguese translation for the terminal feature. [0fc55ab](https://github.com/getumbrel/umbrel/commit/0fc55ab8a0bb3534a8489c109e1a34e251ade24e) <span style='color:grey;'>(significance=0.08)</span>

## ✨ feat
- Settings display IP addresses. [1be5e28](https://github.com/getumbrel/umbrel/commit/1be5e28b329238899d49e77d5f175a7dcd118e55) <span style='color:grey;'>(significance=0.10)</span>

## 🔧 chore
- Finalized umbrelOS 1.2 release: updated version and version name in package.json, adjusted update URLs in the update script to point to the new release. [fc330d5](https://github.com/getumbrel/umbrel/commit/fc330d5ec62bc4a844695234e4802f32c3761a86) <span style='color:grey;'>(significance=0.08)</span>
- Removed console logs and improved code formatting. [7d3f6ac](https://github.com/getumbrel/umbrel/commit/7d3f6ac8aeb231f4a43a5882aca1ff7dae482b30) <span style='color:grey;'>(significance=0.11)</span>
- A new GitHub action manages translations by scanning UI files to remove unused keys, checking for missing variables in non-English locales, removing keys in non-English locales that don't exist in the English locale, generating missing translations, and sorting all locales. [d61acb9](https://github.com/getumbrel/umbrel/commit/d61acb9e25e266922cf37570d0f8918f44db34ce) <span style='color:grey;'>(significance=0.05)</span>
- Translations in locale files sorted alphabetically. Removed unused translations. [209baa9](https://github.com/getumbrel/umbrel/commit/209baa957688c1ba55de827f6507b9c94d1ce5a0) <span style='color:grey;'>(significance=0.07)</span>