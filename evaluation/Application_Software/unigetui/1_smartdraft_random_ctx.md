# 3.1.1
## 🐛 fix
- Addresses a critical issue causing the Widgets server to crash. Modifies the `BuildWidgetsApi` method to format package source display names correctly and updates the `UpdatePackagesForManager` method to handle manager names and display names appropriately. [5f4027e](https://github.com/marticliment/UniGetUI/commit/5f4027e75c8e70175b82625e48e0b6d6d70e8463) 
- Fixed a crash caused by non-sources package managers loading their sources. [5abc216](https://github.com/marticliment/UniGetUI/commit/5abc21668176f649f506f112768866fe1aecae33) 
- Addressed an issue with Package Manager logs not displaying. Modified `TaskLogger` class to implement the `ITaskLogger` interface for proper logging functionality. [87bd9e1](https://github.com/marticliment/UniGetUI/commit/87bd9e14a026a2a17cec86e235ff2a3ad33b14d8) 
- Addresses duplication of local package sources after reloading installed packages. [3952e4a](https://github.com/marticliment/UniGetUI/commit/3952e4ab260f2c59da25bb74f56c32450e7b7599) 
- Addressed incorrect ItemViews rendering by modifying event handling and ensuring proper invalidation and rearrangement of the package list. [8437963](https://github.com/marticliment/UniGetUI/commit/8437963c7f98a6464ce905d10c1964b095e6023b) 
- Refined `PackageItemContainer_RightTapped` method logic. Now checks if the sender is a `PackageItemContainer` and if its `Package` property implements the `IPackage` interface before proceeding with selection and context menu display. [2445248](https://github.com/marticliment/UniGetUI/commit/24452482d7232c7bd1571958be9a65a2877a590e) 
- Addresses an issue where sources wouldn't display the Package Manager name. Adds a method to refresh source names and modifies properties to ensure accurate display based on the current manager's properties. [cf59903](https://github.com/marticliment/UniGetUI/commit/cf599038578b4c6842cced74f1df66c1cca842d1) 
- Notifications are disabled when the System Tray is disabled. [41f8d4a](https://github.com/marticliment/UniGetUI/commit/41f8d4a0bae91f28a8c67e2a2e97af441e24949a) 
- This pull request improves code quality and fixes warnings across the project. Key changes include fixing warnings in core projects and the package engine folder, removing redundant semicolons, string interpolations, and constructors, and correcting typos. The update also simplifies code by replacing multiple if-else statements with single-line return statements and inlining out variable declarations. These changes enhance code readability and maintainability without altering core functionality. [#2531](https://github.com/marticliment/UniGetUI/pull/2531) 

## ✨ feat
- Improved close buttons. [9ed7e4e](https://github.com/marticliment/UniGetUI/commit/9ed7e4e279a558163f87530661c0c6aec87df06d)

## 🔧 chore
- The commit optimizes the WinGet local source parser. Updates the `WinGet` class by changing `LocalSource` properties to `LocalWinGetSource` and refines logic for identifying local sources. Ensures accurate parsing and handling of sources like Local PC, Android Subsystem, Steam, Ubisoft Connect, GOG, and Microsoft Store. [c66c0ea](https://github.com/marticliment/UniGetUI/commit/c66c0ea3610ecea586712fd6b92522cb893eba7a) 
- Improves package search in WinGet by optimizing task management, loading catalogs more efficiently, and enhancing error handling. Reduces redundant operations for a more robust and efficient process. [b185194](https://github.com/marticliment/UniGetUI/commit/b185194e08797993b2cfe6478fc9919cc2ee6e45) 
- Corrected typo in log message from "Fancye exe name" to "Fancy exe name". [2cd6665](https://github.com/marticliment/UniGetUI/commit/2cd66658a3dd42f04656ff76655e8f7de05b1bee) 
- Updated translation percentages, added a new translator, and improved Chinese language files. [07d392d](https://github.com/marticliment/UniGetUI/commit/07d392d4329c2ef86baad4b87bbc339a2af9e4e8)
