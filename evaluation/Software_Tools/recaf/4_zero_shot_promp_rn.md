# Release Notes for Version 2.21.14

## New Features
- **Jadx Mapping File Support**: Added support for Jadx mapping files in the mapping file dialog, enhancing the decompilation mapping capabilities. [#516]
- **UTF-8 Encoding**: FileViewport text mode now uses UTF-8 encoding instead of the default charset, ensuring better text representation. [#524]
- **"itf" Suffix for Invokestatic Calls**: Introduced an "itf" suffix to invokestatic calls to preserve interface method calls, required by the JVM verifier. [#591]
- **Video Explanation**: Added a video explaining the development direction and future plans for Recaf versions 3X and 4X. [Commit 3877b1a]

## Enhancements
- **Performance Improvements**: Optimized the process of reading contents from zip/jar files, resulting in a 2x speed increase. [#761]
- **Dependency Updates**: 
  - Bumped `jsoup` from 1.14.3 to 1.15.3, addressing security and bug fixes. [#599]
  - Updated `com.google.guava:guava` from 31.1-jre to 32.0.0-jre. [#662]
- **New Translations**: Added and optimized Chinese (zh-cn) translations. [#587, #588]
- **Improved Assembler**: New assembler implementation with context menus for instructions and better suggestion handling. [#536, #539]
- **Markdown View**: Introduced a new MarkdownView component for displaying markdown text. [Commit e5669cd]

## Bug Fixes
- **Infinite Loading on Launch**: Fixed an issue causing infinite loading during application startup. [#756]
- **Misspelling Corrections**: Corrected the misspelling of "parameters" in instruction parsers. [#757]
- **Hierarchy Pane**: Fixed the hierarchy pane not being scrollable when a class has many children. [#747]
- **File Export**: Resolved an issue where exported class files had a `.class.class` extension. [#773]
- **Zoom Bug**: Fixed a small zoom bug in the PannableImageView. [#609]

## Removals
- **Auto-Updater**: Removed the auto-updater feature, with a clear indication for users to migrate to version 4.X. [Commit e5669cd]

## Miscellaneous
- **Code Cleanup**: Minor code cleanup and refactoring for better maintainability. [Commit 87695aa]
- **Documentation**: Updated README and documentation to reflect recent changes and improvements. [Commit 3877b1a]

This release includes significant improvements in performance, new features, and important bug fixes, making Recaf more robust and user-friendly. Users are encouraged to update to this version to benefit from these enhancements.