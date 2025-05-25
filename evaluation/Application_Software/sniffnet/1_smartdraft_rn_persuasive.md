# v1.3.1
## 📦 build
- Bumps chrono from 0.4.37 to 0.4.38. This release improves formatting code performance by 20%, introduces a days_since method for the Weekday type, removes the deprecated rustc-serialize feature, and reverts an accidental breaking change in 0.4.36 by switching to derive(Copy) for DateTime. [#509](https://github.com/GyulyVGC/sniffnet/pull/509) <span style='color:grey;'>(significance=0.15)</span>
- Updated rustls dependency from 0.22.3 to 0.22.4. [#513](https://github.com/GyulyVGC/sniffnet/pull/513) <span style='color:grey;'>(significance=0.13)</span>
- Updated `serial_test` dependency. [#517](https://github.com/GyulyVGC/sniffnet/pull/517) <span style='color:grey;'>(significance=0.11)</span>
- Updated serde dependency from 1.0.199 to 1.0.200. [#526](https://github.com/GyulyVGC/sniffnet/pull/526) <span style='color:grey;'>(significance=0.11)</span>
- Bumps toml to 0.8.13. [#537](https://github.com/GyulyVGC/sniffnet/pull/537) <span style='color:grey;'>(significance=0.23)</span>
- Updated etherparse dependency to a minor version. Resolved build error by using correct types from etherparse library. Replaced Ethernet2Header with LinkHeader and adjusted link header handling logic in packet management. [#540](https://github.com/GyulyVGC/sniffnet/pull/540) <span style='color:grey;'>(significance=0.12)</span>
- Fixed preference for literals over escaping double-quotes and resolved deprecations. Removed unused features and updated the changelog. [#545](https://github.com/GyulyVGC/sniffnet/pull/545) <span style='color:grey;'>(significance=0.15)</span>
- Improved functionality and performance. [#562](https://github.com/GyulyVGC/sniffnet/pull/562) <span style='color:grey;'>(significance=0.13)</span>

## 📚 docs
- Abdullah added as a contributor for ideas and content. [#534](https://github.com/GyulyVGC/sniffnet/pull/534) <span style='color:grey;'>(significance=0.11)</span>
- CosminPerRam added as a contributor. [#546](https://github.com/GyulyVGC/sniffnet/pull/546) <span style='color:grey;'>(significance=0.13)</span>
- Added Cornelius Roemer as a contributor for ideas. [#557](https://github.com/GyulyVGC/sniffnet/pull/557) <span style='color:grey;'>(significance=0.11)</span>

## ✨ feat
- Updated Uzbek translations to version 1.3, improving translation strings and adding Uzbek translations for interface elements. Uzbek is now in the list of supported languages. [#510](https://github.com/GyulyVGC/sniffnet/pull/510) <span style='color:grey;'>(significance=0.11)</span>
- Support for the IPinfo MMDB database format, allowing both standard MMDB files and IPinfo's to be imported and used with Sniffnet. New enums for different database entry representations ensure proper deserialization during lookups. Added support for IPinfo database entries with generic MmdbAsnEntry and MmdbCountryEntry, enhancing ASN and country data handling. [#558](https://github.com/GyulyVGC/sniffnet/pull/558) <span style='color:grey;'>(significance=0.22)</span>
- Added keyboard shortcuts to change the zoom level for better user control. [99295e9](https://github.com/GyulyVGC/sniffnet/commit/99295e956858259869ab0112ca3f0405f8b36984) <span style='color:grey;'>(significance=0.19)</span>

## 🐛 fix
- New Polish translations for v1.3 enhance accuracy and consistency. Minor adjustments ensure translations sound more natural. [#498](https://github.com/GyulyVGC/sniffnet/pull/498) <span style='color:grey;'>(significance=0.11)</span>
- Enhanced thumbnail mode with a new keyboard shortcut (Ctrl+T) to toggle the mode, preventing rapid toggling and duplicate entries in the network hosts list. Resolved an issue preventing users from exiting thumbnail mode on Ubuntu. [#512](https://github.com/GyulyVGC/sniffnet/pull/512) <span style='color:grey;'>(significance=0.12)</span>
- The Swedish translation for Sniffnet has been updated to version 1.3, adding support for various terms and phrases across the application and including Swedish in the list of supported languages. [#522](https://github.com/GyulyVGC/sniffnet/pull/522) <span style='color:grey;'>(significance=0.11)</span>
- Optimized translation code by reducing unnecessary `String` allocations. Removed redundant `to_string()` calls and replaced them with more efficient static string references, streamlining the code, improving performance, and enhancing memory usage. [#524](https://github.com/GyulyVGC/sniffnet/pull/524) <span style='color:grey;'>(significance=0.18)</span>
- Increased range of selectable zoom values. [61b6d6b](https://github.com/GyulyVGC/sniffnet/commit/61b6d6b365859d3a7b4c44649dd9b2e9e2cdd037) <span style='color:grey;'>(significance=0.15)</span>
- Adjusted zoom slider step from 0.007 to 0.005 for improved precision. [c34dd6e](https://github.com/GyulyVGC/sniffnet/commit/c34dd6ecdee6f59206946466f0e8cbc700c9f422) <span style='color:grey;'>(significance=0.13)</span>

## 🔧 chore
- Added new German translations and adjusted existing ones for accuracy and consistency. Enhanced readability of the `is_up_to_date` function and introduced a method to check language currency. Updated the language picklist to display warnings for outdated languages. [#495](https://github.com/GyulyVGC/sniffnet/pull/495) <span style='color:grey;'>(significance=0.11)</span>
- Images optimized for better performance. [#508](https://github.com/GyulyVGC/sniffnet/pull/508) <span style='color:grey;'>(significance=0.11)</span>
- The v1.3.1 release of Sniffnet includes support for IPinfo ASN and Country databases, new keyboard shortcuts for zoom level adjustments, and an increased range of selectable zoom values. Addresses an issue preventing exit from thumbnail mode on some Linux distributions and reduces `String` allocations in translation code. Introduces new service entries and refines the handling of ASN and country entries. [#564](https://github.com/GyulyVGC/sniffnet/pull/564) <span style='color:grey;'>(significance=0.10)</span>
- Updated dependencies. [461486f](https://github.com/GyulyVGC/sniffnet/commit/461486f4d7d347b2c36197e6105fcc629c413912) <span style='color:grey;'>(significance=0.13)</span>
- Various improvements and optimizations. [d113c26](https://github.com/GyulyVGC/sniffnet/commit/d113c26376ba1397ceb506277e23170c762cbef9) <span style='color:grey;'>(significance=0.13)</span>
- Added "pmsm-webrctl" to the list of safe words for service names. [91c5f31](https://github.com/GyulyVGC/sniffnet/commit/91c5f31ceb258c3caac599307ea25dd064f09eb4) <span style='color:grey;'>(significance=0.11)</span>