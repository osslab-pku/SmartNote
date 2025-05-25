# v1.3.1
## feat
- Introduced Ctrl+T shortcut to toggle thumbnail mode. Resolved issue preventing exit from thumbnail mode on Ubuntu. Fixed duplicated entries in the network hosts list by adding a `ThumbnailHost` struct to uniquely represent network hosts. [#512](https://github.com/GyulyVGC/sniffnet/pull/512) <span style='color:grey;'>(significance=0.41)</span>
- Preparing for Sniffnet v1.3.1 release. Fixes for Clippy pedantic lints enhance code quality and adherence to Rust's best practices. Updated the upper layer service list with new services and adjusted the total count. [#564](https://github.com/GyulyVGC/sniffnet/pull/564) <span style='color:grey;'>(significance=0.45)</span>
- Introduced Persian translation; right-to-left (RTL) text support not yet available. [9163e95](https://github.com/GyulyVGC/sniffnet/commit/9163e95e5b3eedb93958800c178782fb2a7bbd64) <span style='color:grey;'>(significance=0.32)</span>
- Updated Uzbek translations. [#510](https://github.com/GyulyVGC/sniffnet/pull/510) <span style='color:grey;'>(significance=0.25)</span>
- Increased range of selectable zoom values. [61b6d6b](https://github.com/GyulyVGC/sniffnet/commit/61b6d6b365859d3a7b4c44649dd9b2e9e2cdd037) <span style='color:grey;'>(significance=0.25)</span>
- Added keyboard shortcuts to change the zoom level, enhancing user control over the interface. [99295e9](https://github.com/GyulyVGC/sniffnet/commit/99295e956858259869ab0112ca3f0405f8b36984) <span style='color:grey;'>(significance=0.16)</span>

## fix
- Support for IPinfo MMDB database format added, allowing import and use with Sniffnet. New enums introduced for database entry representations, ensuring proper deserialization. `MmdbAsnEntry` struct now supports different ASN formats with a `get_asn` method. `MmdbReader` struct enhanced with a `lookup` method for easier querying of ASN and country information. Support for IPinfo database entries extended with `MmdbCountryEntry`, including country lookup modifications and new modules for handling various country entries. [#558](https://github.com/GyulyVGC/sniffnet/pull/558) <span style='color:grey;'>(significance=0.44)</span>
- Updated etherparse from 0.14.3 to 0.15.0, adding Linux SLL support and fixing the SlicedPacket::from_ether_type function to correctly set the link field. [#540](https://github.com/GyulyVGC/sniffnet/pull/540) <span style='color:grey;'>(significance=0.14)</span>
- Created a script to subset font files to include only necessary glyphs. [2cb90fa](https://github.com/GyulyVGC/sniffnet/commit/2cb90fadd9d2bffa47721ab171d6d7e40a1300b3) <span style='color:grey;'>(significance=0.17)</span>
- Introduced Romanian translations, enhancing multilingual support. [#499](https://github.com/GyulyVGC/sniffnet/pull/499) <span style='color:grey;'>(significance=0.16)</span>

## perf
- Images optimized, resulting in a 29% reduction in file size to improve performance. [#508](https://github.com/GyulyVGC/sniffnet/pull/508) <span style='color:grey;'>(significance=0.14)</span>
- Optimized translation code by replacing `String` with static string references, improving memory allocation and translation function efficiency. Addressed formatting issues for better readability. [#524](https://github.com/GyulyVGC/sniffnet/pull/524) <span style='color:grey;'>(significance=0.43)</span>
- Addresses new Clippy lints and includes code improvements. Refines configuration handling with `clone_from` for better performance and clarity. Updates dependencies to their latest versions for compatibility and latest features. [f3acc04](https://github.com/GyulyVGC/sniffnet/commit/f3acc041e589e75730ec018b48c8b423df700e97) <span style='color:grey;'>(significance=0.43)</span>
- Adjusted zoom slider step for improved precision. [c34dd6e](https://github.com/GyulyVGC/sniffnet/commit/c34dd6ecdee6f59206946466f0e8cbc700c9f422) <span style='color:grey;'>(significance=0.40)</span>

## build
- Updated plotters dependency with enhancements and bug fixes. Added Clone and PartialEq traits to SeriesLabelPosition and ShapeStyle, a function to draw and save an evcxr figure, and a dotted line style. Fixed issues with infinite size for collinear line segments, overflow in blit_bitmap, and the dashed line algorithm. [#538](https://github.com/GyulyVGC/sniffnet/pull/538) <span style='color:grey;'>(significance=0.37)</span>
- Bumped rodio dependency from 0.18.0 to 0.18.1, fixing a hang issue when seeking with an empty sink. [#539](https://github.com/GyulyVGC/sniffnet/pull/539) <span style='color:grey;'>(significance=0.40)</span>
- Updated project dependencies. [64cf251](https://github.com/GyulyVGC/sniffnet/commit/64cf251b013cc6f87b71d350b310be26728aec0a) <span style='color:grey;'>(significance=0.38)</span>
- Added new sample theme "sniffnet_rebrand.toml." [fad521a](https://github.com/GyulyVGC/sniffnet/commit/fad521a8f5fb41e260ee0bdada53633a3d72a560) <span style='color:grey;'>(significance=0.38)</span>
- Addressed new Clippy lints with code adjustments. Corrected `default-features` syntax in `Cargo.toml`. Added conditional compilation attributes for the `desc` field in the `MyDevice` struct and related implementations, including it only for Windows. [24f1623](https://github.com/GyulyVGC/sniffnet/commit/24f1623b155dee5beca7bc0162a955eeb8100f01) <span style='color:grey;'>(significance=0.33)</span>
- Updated various dependencies for compatibility, latest improvements, and bug fixes. [d113c26](https://github.com/GyulyVGC/sniffnet/commit/d113c26376ba1397ceb506277e23170c762cbef9) <span style='color:grey;'>(significance=0.14)</span>
- Updated `chrono` dependency from 0.4.37 to 0.4.38. [#509](https://github.com/GyulyVGC/sniffnet/pull/509) <span style='color:grey;'>(significance=0.10)</span>
- Updated serde dependency. [#511](https://github.com/GyulyVGC/sniffnet/pull/511) <span style='color:grey;'>(significance=0.12)</span>
- Minor improvements and bug fixes. [#513](https://github.com/GyulyVGC/sniffnet/pull/513) <span style='color:grey;'>(significance=0.29)</span>
- Updated pcap dependency from 1.3.0 to 2.0.0. [#516](https://github.com/GyulyVGC/sniffnet/pull/516) <span style='color:grey;'>(significance=0.19)</span>
- Upgraded serde dependency from version 1.0.199 to 1.0.200. [#526](https://github.com/GyulyVGC/sniffnet/pull/526) <span style='color:grey;'>(significance=0.19)</span>
- Updated serde library to provide public access to RenameAllRules in serde_derive_internals. [#536](https://github.com/GyulyVGC/sniffnet/pull/536) <span style='color:grey;'>(significance=0.16)</span>
- Bumped `toml` crate from 0.8.12 to 0.8.13. [#537](https://github.com/GyulyVGC/sniffnet/pull/537) <span style='color:grey;'>(significance=0.44)</span>
- Bumps serde to 1.0.203. [#541](https://github.com/GyulyVGC/sniffnet/pull/541) <span style='color:grey;'>(significance=0.24)</span>
- Updated `rstest` dependency. [#544](https://github.com/GyulyVGC/sniffnet/pull/544) <span style='color:grey;'>(significance=0.12)</span>
- Updated toml library. [#545](https://github.com/GyulyVGC/sniffnet/pull/545) <span style='color:grey;'>(significance=0.41)</span>
- Bumps serde from 1.0.203 to 1.0.204. Applies #[diagnostic::on_unimplemented] attribute on Rust 1.78+ to suggest adding serde derive or enabling a "serde" feature flag in dependencies. [#559](https://github.com/GyulyVGC/sniffnet/pull/559) <span style='color:grey;'>(significance=0.13)</span>
- Bumps toml from 0.8.14 to 0.8.15. [#562](https://github.com/GyulyVGC/sniffnet/pull/562) <span style='color:grey;'>(significance=0.37)</span>

## docs
- Added Russian translation v3 and corrected previous errors. [#496](https://github.com/GyulyVGC/sniffnet/pull/496) <span style='color:grey;'>(significance=0.29)</span>
- Introduces Japanese translations for UI elements, addresses merge conflicts, adds new contributors, and updates translations. Adds a script for subsetting font files and refines configuration settings and database paths. [#504](https://github.com/GyulyVGC/sniffnet/pull/504) <span style='color:grey;'>(significance=0.32)</span>
- Added new translation for v1.3 release. Tweaked existing translations for consistency and naturalness. Introduced Polish translations for various user interface elements, enhancing accessibility for Polish-speaking users. [#498](https://github.com/GyulyVGC/sniffnet/pull/498) <span style='color:grey;'>(significance=0.32)</span>
- Updated SECURITY.md to support version 1.3.x and remove support for versions below 1.3. Streamlined guidelines for reporting vulnerabilities by removing out-of-scope vulnerabilities list and simplifying reporting instructions. [68aac1e](https://github.com/GyulyVGC/sniffnet/commit/68aac1ed86fca2a670aae5dbada8d90807064d6c) <span style='color:grey;'>(significance=0.27)</span>
- Updated cargo install instructions to include the `--locked` flag. [d6d3c27](https://github.com/GyulyVGC/sniffnet/commit/d6d3c273329aef9722493a4b4f746759c92b6cac) <span style='color:grey;'>(significance=0.16)</span>
- Added Dinozavvvr for translation contributions. [#519](https://github.com/GyulyVGC/sniffnet/pull/519) <span style='color:grey;'>(significance=0.13)</span>
- Added Abdullah as a contributor for ideas and content. [#534](https://github.com/GyulyVGC/sniffnet/pull/534) <span style='color:grey;'>(significance=0.14)</span>
- Added CosminPerRam as a contributor. [#546](https://github.com/GyulyVGC/sniffnet/pull/546) <span style='color:grey;'>(significance=0.10)</span>

## chore
- Introduced French translation for v1.3, enhancing multilingual support. [#494](https://github.com/GyulyVGC/sniffnet/pull/494) <span style='color:grey;'>(significance=0.19)</span>
- Added new German translations and adjusted existing ones. Enhanced language picklist to notify users if a selected language is not fully updated. [#495](https://github.com/GyulyVGC/sniffnet/pull/495) <span style='color:grey;'>(significance=0.19)</span>
- Updated Swedish translation for Sniffnet to version 1.3, adding missing translations and removing the outdated warning. [#522](https://github.com/GyulyVGC/sniffnet/pull/522) <span style='color:grey;'>(significance=0.24)</span>
- Added `track_position` to track duration since the beginning of the source. Fixed Mp4a issue where decodable tracks after undecodable tracks now play correctly, matching VLC's behavior. [#550](https://github.com/GyulyVGC/sniffnet/pull/550) <span style='color:grey;'>(significance=0.31)</span>
- Includes various dependency updates and improvements. [461486f](https://github.com/GyulyVGC/sniffnet/commit/461486f4d7d347b2c36197e6105fcc629c413912) <span style='color:grey;'>(significance=0.14)</span>
- Added "pmsm-webrctl" to the list of safe words for service names. [91c5f31](https://github.com/GyulyVGC/sniffnet/commit/91c5f31ceb258c3caac599307ea25dd064f09eb4) <span style='color:grey;'>(significance=0.20)</span>