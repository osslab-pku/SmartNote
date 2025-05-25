## Improvements
- Pattern hover highlighting performance has been drastically improved
- Completely eradicated any Window flickering during resizes on Windows and the Web
- Toolbar items now have tooltips
- The web version can now be properly used on mobile and with touch inputs
- Custom plugins can once again be built using the SDK
- File dialogs now belong to the ImHex window on Linux. Thanks a lot to @btzy 

## Bug Fixes
- Fixed a crash that triggered when an auto backup was being created on macOS
- Fixed liblzma not being configured in correctly on all OSes
- Having debug mode enabled in a pattern no longer makes the UI lag out after evaluation
- The find and goto popups no longer go transparent when opening a combo box within them
- Fixed a rare crash when re-evaluating patterns while a sorting option was selected

## Pattern Language
- Added builtin crc8, crc16 and crc64 hash functions
- The crc functions can now also be used with strings 
- Fixed a bug where patterns passed to non-type template parameters would get hidden
- std::mem::find_sequence and co are now HUNDREDS of times faster. This includes std::mem::MagicSearcher

# Previous Release 

## Additions
- Added basic process memory provider support to macOS
    - Due to limitations on Apple's side, this only works with SIP disabled
- View providers can now be renamed
- Added options to load files into memory or read data from disk instead, independent of the file size
- Find results can now be exported as CSVs, TSVs and JSONs. Thanks a lot to @SparkyTD
- Added various per-byte highlights to the hex editor minimap
    - The minimap can now display the highlighting of individual bytes
- Added a digital signal pattern visualizer
- The pattern data view now uses nicer colors and strings to convey information
- The recent files section on the welcome screen can now be collapsed
- You can now scroll the hex editor view faster by holding down CTRL or even faster when holding down SHIFT + CTRL
- Added a `--reset-settings` CLI command to clear all settings in case something gets corrupted

## Improvements
- **Drastically improved rendering times**
- Added a small moon icon to the welcome screen in nightly builds
- Providers now close instantly
- The hex editor view no longer scrolls when jumping to a selection that's already visible
- Auto project backups are now enabled by default
- Custom data inspector rows now display a nice error message in the UI when they encountered an error
- Bookmark reordering now doesn't swap entries anymore and actually works as expected
- ImHex now displays a little dot in the close button on macOS if there's unsaved changes
- Auto backups no longer remove the dirty status of providers anymore
- SIGINT signals are now being handled to not close ImHex immediately anymore but to show a popup
- UI scaling factors are now limited between 0.1x and 4.0x to prevent issues
    - Larger values are still possible by CTRL-clicking into the slider and entering a value manually
- PageUp + PageDown no longer affects the hex editor selection
- Row highlighting in the pattern data view is now less bright so the text has a better contrast

## Bug Fixes
- ImHex can now properly load files stored on network drives on Windows
- Fixed crashes when searching for certain regex strings
- Fixed an infinite loop when searching forward/backward with CTRL + F
- Fixed loading of layout files
- Fixed fonts being blurry in some cases
- Bookmark regions can now be set to 1 byte
- Fixes Alt and Ctrl being swapped in the text editor on macOS
- Fixed disassembler always disassembling in little endian
- ImHex no longer tries to store files in system paths now
- Fixed an infinite loop when exporting data selections to a file. Thanks a lot to @FireNX70
- Fixed file name display issues with files that contain unicode characters
- Fixed content store getting stuck sometimes when updating multiple items at once

## Pattern Language 
- `continue` and `break` now work as one would expect
- Added `std::core::execute_function()`
- Arrays can now be initialized using the following syntax:
    - `u32 myArray[5] = { 1, 2, 3, 4, 5 };`
- Added support for constants inside of custom types
- Unsigned, signed and floating point patterns no longer display their hex value in their value by default
- Fixed [[no_unique_address]] not working correctly with bitfields
- Patterns are now highlighted in the hex editor view when hovering over them in the pattern data view
- Patterns in the pattern data view table are now highlighted when they are fully selected in the hex editor view
- Bitfields can now be properly edited in the pattern data view
- The filter in the pattern data view now gets correctly applied again after re-evaluating a pattern

<br/>

<p align="center">If you like my work, please consider supporting me on GitHub Sponsors, Patreon or PayPal. Thanks a lot!</p>
<p align="center">
<a href="https://github.com/sponsors/WerWolv"><img src="https://werwolv.net/assets/github_banner.png" alt="GitHub donate button" /> </a>
<a href="https://www.patreon.com/werwolv"><img src="https://c5.patreon.com/external/logo/become_a_patron_button.png" alt="Patreon donate button" /> </a>
<a href="https://werwolv.net/donate"><img src="https://werwolv.net/assets/paypal_banner.png" alt="PayPal donate button" /> </a>
</p