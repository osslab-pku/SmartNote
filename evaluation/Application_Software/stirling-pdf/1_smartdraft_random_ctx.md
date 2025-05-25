# v0.28.0
## 🛠️ breaking changes
- Updated `remove-pages.html` to replace a redundant file selector with a text input field for specifying page numbers to delete. [f165439](https://github.com/Stirling-Tools/Stirling-PDF/commit/f165439d2614f321e897e64829c1e6073e09e28e) 

## ✨ feat
- Ensures tessdata availability to local users on Windows systems. [#1677](https://github.com/Stirling-Tools/Stirling-PDF/pull/1677) 
- Enhanced admin panel with improved user management: disable/enable users and track activity. Fixed SSO login issues due to faulty verification. Improved and translated error messages for better user experience. [#1658](https://github.com/Stirling-Tools/Stirling-PDF/pull/1658) 

## 🐛 fix
- Fixed a bug in conditional binding of the "multiple" attribute in the file selector fragment, ensuring correct functionality of the file input element. [#1665](https://github.com/Stirling-Tools/Stirling-PDF/pull/1665) 
- Updated the Italian localization file, `messages_it_IT.properties`, correcting the translation for the "Remove image" feature in the home section. The title and description for removing images from PDFs are now consistent and clear for Italian-speaking users. [#1661](https://github.com/Stirling-Tools/Stirling-PDF/pull/1661) 

## 📦 build
- Updated build configuration to use common version variables for dependencies. [#1697](https://github.com/Stirling-Tools/Stirling-PDF/pull/1697) 
- Simplified build workflow configuration by removing conditional checks and labels for specific events and branches. [8602f38](https://github.com/Stirling-Tools/Stirling-PDF/commit/8602f38fbff87205fc09a79fb0a0407e43e1e13d) 
- Updated build.gradle file. [9773138](https://github.com/Stirling-Tools/Stirling-PDF/commit/97731386121a99adba450f98ea93d1b1bdfbb213) 
- Minor patch to the logback-classic library, enhancing logging framework stability and performance. [#1685](https://github.com/Stirling-Tools/Stirling-PDF/pull/1685) 

## 🔧 chore
- Updated the dependabot configuration to limit open pull requests to 10. [909054a](https://github.com/Stirling-Tools/Stirling-PDF/commit/909054a49d8b3befa25d81682e9ab7528cbea257) 
- Updated the dependabot configuration file to set the rebase strategy to "auto" for the weekly update schedule. [6fa7c2e](https://github.com/Stirling-Tools/Stirling-PDF/commit/6fa7c2e5e128b23658ea6203444f46b2bae89b95) 
- Enhanced GitHub Actions workflows: updated build and auto-labeler configurations, removed test workflow. [#1693](https://github.com/Stirling-Tools/Stirling-PDF/pull/1693) 
- Updated auto-labeler workflow permissions by removing 'workflows: write' permission. [8997855](https://github.com/Stirling-Tools/Stirling-PDF/commit/8997855922af45ff8b6a6d15373e893d7e441a10) 
- The build workflow now triggers on pushes to the main branch and after the "Pull Request Labeler" workflow. Conditions for running build and docker-compose-tests jobs now check for specific labels on pull requests. Permissions for actions, contents, and security-events have been set. Introduced a matrix strategy for JDK versions 17 and 21. [e89ac84](https://github.com/Stirling-Tools/Stirling-PDF/commit/e89ac84928c48ba4a337ced96c6886fefb69df81) 
- Updated java-security-toolkit dependency to improve security features. [#1667](https://github.com/Stirling-Tools/Stirling-PDF/pull/1667) 
- Updated org.springframework:spring-webmvc dependency from 6.1.9 to 6.1.12. [#1680](https://github.com/Stirling-Tools/Stirling-PDF/pull/1680) 
- Updated org.apache.pdfbox:pdfbox dependency. [#1691](https://github.com/Stirling-Tools/Stirling-PDF/pull/1691) 
- Updated the dependency-license-report plugin to a minor version. [#1690](https://github.com/Stirling-Tools/Stirling-PDF/pull/1690) 
- Updated third-party licenses. [#1687](https://github.com/Stirling-Tools/Stirling-PDF/pull/1687) [#1695](https://github.com/Stirling-Tools/Stirling-PDF/pull/1695) [#1696](https://github.com/Stirling-Tools/Stirling-PDF/pull/1696) [#1698](https://github.com/Stirling-Tools/Stirling-PDF/pull/1698) 
- Updated a dependency. [#1686](https://github.com/Stirling-Tools/Stirling-PDF/pull/1686) [#1689](https://github.com/Stirling-Tools/Stirling-PDF/pull/1689) 
- Updated workflow configuration to include an auto-approve step for new pull requests and ensure the auto-merge step executes only if a pull request is created. [ea2d755](https://github.com/Stirling-Tools/Stirling-PDF/commit/ea2d7558081b9ce62acf994ad60fc5c6a9b2e17d) 
- Redesigned footer includes a new links section with styled links for "Licenses" and "Survey." Updated layout and styling improve appearance and usability. [#1674](https://github.com/Stirling-Tools/Stirling-PDF/pull/1674) 
- Updated Japanese translation for accurate and consistent localization of UI elements and messages. [#1654](https://github.com/Stirling-Tools/Stirling-PDF/pull/1654) 
- Updated Brazilian Portuguese translation for interface elements like prompts, buttons, and messages, enhancing accessibility and user-friendliness. [#1673](https://github.com/Stirling-Tools/Stirling-PDF/pull/1673) 
- Minor improvements and bug fixes. [#1670](https://github.com/Stirling-Tools/Stirling-PDF/pull/1670) [#1684](https://github.com/Stirling-Tools/Stirling-PDF/pull/1684) 
- Improvements and optimizations. [#1683](https://github.com/Stirling-Tools/Stirling-PDF/pull/1683) 

## 📚 docs
- Updated Italian translation progress from 98% to 99%. [#1651](https://github.com/Stirling-Tools/Stirling-PDF/pull/1651) 
- The translation progress table in the README now shows the Portuguese Brazilian translation increased from 59% to 85%. [#1675](https://github.com/Stirling-Tools/Stirling-PDF/pull/1675) 
- Updated Japanese translation progress in the README from 89% to 92%. [#1655](https://github.com/Stirling-Tools/Stirling-PDF/pull/1655)
