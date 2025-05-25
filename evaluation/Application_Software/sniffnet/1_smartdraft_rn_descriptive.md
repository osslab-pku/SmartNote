# v1.3.1
## 📦 build
- Updated `chrono` dependency with 20% performance improvement in formatting code. Introduced `days_since` method for `Weekday` type. Removed deprecated `rustc-serialize` feature and reverted accidental breaking change related to `derive(Copy)` for `DateTime`. Added `TimeDelta::checked_mul` and `TimeDelta::checked_div` methods. Fixed error when rounding with a zero duration. [#509](https://github.com/GyulyVGC/sniffnet/pull/509) <span style='color:grey;'>(significance=0.15)</span>
- Updated `toml` dependency. [#537](https://github.com/GyulyVGC/sniffnet/pull/537) <span style='color:grey;'>(significance=0.23)</span> [#545](https://github.com/GyulyVGC/sniffnet/pull/545) <span style='color:grey;'>(significance=0.15)</span> [#562](https://github.com/GyulyVGC/sniffnet/pull/562) <span style='color:grey;'>(significance=0.13)</span>
- Bumps rustls from 0.22.3 to 0.22.4. [#513](https://github.com/GyulyVGC/sniffnet/pull/513) <span style='color:grey;'>(significance=0.13)</span>
- Bumped etherparse from 0.14.3 to 0.15.0. Added Linux SLL support and fixed SlicedPacket::from_ether_type bug to ensure correct link field setting. [#540](https://github.com/GyulyVGC/sniffnet/pull/540) <span style='color:grey;'>(significance=0.12)</span>
- Bumps `serial_test` to 3.1.0. [#517](https://github.com/GyulyVGC/sniffnet/pull/517) <span style='color:grey;'>(significance=0.11)</span>
- Updated `serde` dependency. [#526](https://github.com/GyulyVGC/sniffnet/pull/526) <span style='color:grey;'>(significance=0.11)</span>

## 🔧 chore
- Updated various dependencies for compatibility and latest improvements. [461486f](https://github.com/GyulyVGC/sniffnet/commit/461486f4d7d347b2c36197e6105fcc629c413912) <span style='color:grey;'>(significance=0.13)</span> [d113c26](https://github.com/GyulyVGC/sniffnet/commit/d113c26376ba1397ceb506277e23170c762cbef9) <span style='color:grey;'>(significance=0.13)</span>
- Added new and adjusted existing German translations for better localization. [#495](https://github.com/GyulyVGC/sniffnet/pull/495) <span style='color:grey;'>(significance=0.11)</span>
- Images optimized, resulting in a 29% reduction in file size. [#508](https://github.com/GyulyVGC/sniffnet/pull/508) <span style='color:grey;'>(significance=0.11)</span>
- Added "pmsm-webrctl" to the list of safe words for service names. [91c5f31](https://github.com/GyulyVGC/sniffnet/commit/91c5f31ceb258c3caac599307ea25dd064f09eb4) <span style='color:grey;'>(significance=0.11)</span>
- Preparing for Sniffnet v1.3.1 release. This update includes improvements to thumbnail mode, support for IPinfo ASN and Country databases, new keyboard shortcuts for zoom level adjustments, and an increased range of selectable zoom values. It addresses the issue of exiting thumbnail mode on some Linux distributions and reduces `String` allocations in translation code. Several translations have been updated, and Clippy pedantic lints have been addressed by refining match patterns and string handling. [#564](https://github.com/GyulyVGC/sniffnet/pull/564) <span style='color:grey;'>(significance=0.10)</span>

## ✨ feat
- Support for the IPinfo MMDB database format added, allowing both standard MMDB files and IPinfo's to be imported and used with Sniffnet. New enums for different database entry representations ensure proper deserialization during lookups. Tests for `get_asn()` and `get_country()` functions added, and a new `lookup` method introduced to the `MmdbReader` struct, streamlining ASN and country queries from the MaxMind database. [#558](https://github.com/GyulyVGC/sniffnet/pull/558) <span style='color:grey;'>(significance=0.22)</span>
- Added keyboard shortcuts to change the zoom level, enhancing user control over the interface. [99295e9](https://github.com/GyulyVGC/sniffnet/commit/99295e956858259869ab0112ca3f0405f8b36984) <span style='color:grey;'>(significance=0.19)</span>
- Updated translations for version 1.3, adding support for Uzbek. [#510](https://github.com/GyulyVGC/sniffnet/pull/510) <span style='color:grey;'>(significance=0.11)</span>

## 🐛 fix
- Optimized translation code by reducing unnecessary `String` usage. Removed redundant `to_string()` calls and replaced per-item `.to_string()` with an entire match block `.to_string()`, streamlining code and enhancing performance. Addressed formatting issues for improved readability and maintainability. [#524](https://github.com/GyulyVGC/sniffnet/pull/524) <span style='color:grey;'>(significance=0.18)</span>
- Increased range of selectable zoom values. [61b6d6b](https://github.com/GyulyVGC/sniffnet/commit/61b6d6b365859d3a7b4c44649dd9b2e9e2cdd037) <span style='color:grey;'>(significance=0.15)</span>
- Adjusted zoom slider step for improved precision. [c34dd6e](https://github.com/GyulyVGC/sniffnet/commit/c34dd6ecdee6f59206946466f0e8cbc700c9f422) <span style='color:grey;'>(significance=0.13)</span>
- Enhanced thumbnail mode by fixing an issue preventing users from exiting on Linux, adding a keyboard shortcut (Ctrl+T) to toggle, and ensuring no duplicate entries in the network hosts list. [#512](https://github.com/GyulyVGC/sniffnet/pull/512) <span style='color:grey;'>(significance=0.12)</span>
- Updated Polish translations for v1.3, enhancing localization support and resolving conflicts after rebase. [#498](https://github.com/GyulyVGC/sniffnet/pull/498) <span style='color:grey;'>(significance=0.11)</span>
- The Swedish translation for Sniffnet has been updated to version 1.3, adding support for various terms and phrases and removing the outdated translation warning. [#522](https://github.com/GyulyVGC/sniffnet/pull/522) <span style='color:grey;'>(significance=0.11)</span>

## 📚 docs
- Added CosminPerRam as a contributor. [#546](https://github.com/GyulyVGC/sniffnet/pull/546) <span style='color:grey;'>(significance=0.13)</span>
- Abdullah added as a contributor for ideas and content. [#534](https://github.com/GyulyVGC/sniffnet/pull/534) <span style='color:grey;'>(significance=0.11)</span>
- Cornelius Roemer added as a contributor for ideas. [#557](https://github.com/GyulyVGC/sniffnet/pull/557) <span style='color:grey;'>(significance=0.11)</span>