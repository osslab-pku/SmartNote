# v0.28.0
## ✨ feat
- Ensures tessdata availability to local users by introducing a configurable directory path for tessdata files. [#1677](https://github.com/Stirling-Tools/Stirling-PDF/pull/1677) <span style='color:grey;'>(significance=0.31)</span>
- Enhanced user management in the admin panel: prevents SSO login due to faulty verification, improves error message display, adds translation support, blocks SSO registration without prior admin approval, and includes various UI improvements for better user experience. [#1658](https://github.com/Stirling-Tools/Stirling-PDF/pull/1658) <span style='color:grey;'>(significance=0.68)</span>

## 🐛 fix
- Addressed a conditional attribute binding issue for the "multiple" attribute in the file selector fragment. [#1665](https://github.com/Stirling-Tools/Stirling-PDF/pull/1665) <span style='color:grey;'>(significance=0.37)</span>
- Localization update for the Italian language properties file: modified titles, descriptions, and tags for the "Remove image" feature in the home section. [#1661](https://github.com/Stirling-Tools/Stirling-PDF/pull/1661) <span style='color:grey;'>(significance=0.24)</span>

## 🔧 chore
- Updated Japanese translation for accurate and consistent language in UI elements and messages. [#1654](https://github.com/Stirling-Tools/Stirling-PDF/pull/1654) <span style='color:grey;'>(significance=0.40)</span>
- Translation progress for Japanese updated from 89% to 92%. [#1655](https://github.com/Stirling-Tools/Stirling-PDF/pull/1655) <span style='color:grey;'>(significance=0.38)</span>
- Redesigned footer for improved layout and functionality. Added a new links section with styled "Licenses" and "Survey" links. Adjusted padding for better visual alignment. Updated CSS with a new class for consistent footer link styling. [#1674](https://github.com/Stirling-Tools/Stirling-PDF/pull/1674) <span style='color:grey;'>(significance=0.27)</span>
- Updated `dependabot.yml` to limit open pull requests to 10. [909054a](https://github.com/Stirling-Tools/Stirling-PDF/commit/909054a49d8b3befa25d81682e9ab7528cbea257) <span style='color:grey;'>(significance=0.26)</span>
- Rebase strategy set to "auto" in dependabot configuration. [6fa7c2e](https://github.com/Stirling-Tools/Stirling-PDF/commit/6fa7c2e5e128b23658ea6203444f46b2bae89b95) <span style='color:grey;'>(significance=0.26)</span>
- Updated third-party licenses. [#1687](https://github.com/Stirling-Tools/Stirling-PDF/pull/1687) <span style='color:grey;'>(significance=0.26)</span> [#1695](https://github.com/Stirling-Tools/Stirling-PDF/pull/1695) <span style='color:grey;'>(significance=0.29)</span>
- Updated GitHub Actions workflows: build and auto-labeler configurations enhanced. Removed test workflow. Added steps to the build process for improved automation and efficiency. [#1693](https://github.com/Stirling-Tools/Stirling-PDF/pull/1693) <span style='color:grey;'>(significance=0.17)</span>
- Adjusted permissions for workflows in the auto-labeler configuration. [8997855](https://github.com/Stirling-Tools/Stirling-PDF/commit/8997855922af45ff8b6a6d15373e893d7e441a10) <span style='color:grey;'>(significance=0.22)</span>
- The build workflow now triggers on pushes to the main branch and after the "Pull Request Labeler" workflow. Conditions for running build and docker-compose-tests jobs now check for specific labels on pull requests, excluding 'licenses'. Permissions for actions, contents, and security-events are set. Introduced a matrix strategy for JDK versions 17 and 21. [e89ac84](https://github.com/Stirling-Tools/Stirling-PDF/commit/e89ac84928c48ba4a337ced96c6886fefb69df81) <span style='color:grey;'>(significance=0.19)</span>
- Enhanced the license update workflow to include auto-approval for new pull requests. Updated auto-merge functionality to use the latest version of the relevant GitHub action. [ea2d755](https://github.com/Stirling-Tools/Stirling-PDF/commit/ea2d7558081b9ce62acf994ad60fc5c6a9b2e17d) <span style='color:grey;'>(significance=0.20)</span>
- Modified 3rd Party Licenses: adjusted module versions for "ch.qos.logback:logback-classic" and "ch.qos.logback:logback-core". [#1696](https://github.com/Stirling-Tools/Stirling-PDF/pull/1696) <span style='color:grey;'>(significance=0.27)</span>
- Updated the edu.sc.seis.launch4j plugin. [#1686](https://github.com/Stirling-Tools/Stirling-PDF/pull/1686) <span style='color:grey;'>(significance=0.23)</span>
- Updated the Spring Web MVC library version, enhancing stability and performance. [#1680](https://github.com/Stirling-Tools/Stirling-PDF/pull/1680) <span style='color:grey;'>(significance=0.21)</span>
- Minor patch to the micrometer-core library, enhancing performance and stability. [#1689](https://github.com/Stirling-Tools/Stirling-PDF/pull/1689) <span style='color:grey;'>(significance=0.19)</span>
- Updated Brazilian Portuguese translation for improved accuracy and clarity in UI elements, including prompts, messages, and labels. [#1673](https://github.com/Stirling-Tools/Stirling-PDF/pull/1673) <span style='color:grey;'>(significance=0.17)</span>
- Minor change included. [#1670](https://github.com/Stirling-Tools/Stirling-PDF/pull/1670) <span style='color:grey;'>(significance=0.20)</span>
- Enhanced security toolkit with latest improvements and fixes. [#1667](https://github.com/Stirling-Tools/Stirling-PDF/pull/1667) <span style='color:grey;'>(significance=0.12)</span>
- Improvements to the codebase. [#1684](https://github.com/Stirling-Tools/Stirling-PDF/pull/1684) <span style='color:grey;'>(significance=0.25)</span>
- Improvements and optimizations to core functionality. [#1683](https://github.com/Stirling-Tools/Stirling-PDF/pull/1683) <span style='color:grey;'>(significance=0.21)</span>
- Includes minor improvements and optimizations. [#1690](https://github.com/Stirling-Tools/Stirling-PDF/pull/1690) <span style='color:grey;'>(significance=0.27)</span>
- Modified remove-pages.html to replace a redundant file selector with a text input field for specifying page numbers, enhancing the user interface. [f165439](https://github.com/Stirling-Tools/Stirling-PDF/commit/f165439d2614f321e897e64829c1e6073e09e28e) <span style='color:grey;'>(significance=0.25)</span>

## 📦 build
- Updated build configuration to enhance security. [#1685](https://github.com/Stirling-Tools/Stirling-PDF/pull/1685) <span style='color:grey;'>(significance=0.29)</span>
- Updated build configuration to use common version variables for dependencies. [#1697](https://github.com/Stirling-Tools/Stirling-PDF/pull/1697) <span style='color:grey;'>(significance=0.30)</span>
- Updated the project version in build.gradle from 0.27.0 to 0.28.0. [9773138](https://github.com/Stirling-Tools/Stirling-PDF/commit/97731386121a99adba450f98ea93d1b1bdfbb213) <span style='color:grey;'>(significance=0.16)</span>
- Updated application version from 0.27.0 to 0.28.0. [#1699](https://github.com/Stirling-Tools/Stirling-PDF/pull/1699) <span style='color:grey;'>(significance=0.11)</span>

## 📚 docs
- Translation progress for Italian updated from 98% to 99%. [#1651](https://github.com/Stirling-Tools/Stirling-PDF/pull/1651) <span style='color:grey;'>(significance=0.33)</span>
- Updated Brazilian Portuguese translation progress from 59% to 85%. [#1675](https://github.com/Stirling-Tools/Stirling-PDF/pull/1675) <span style='color:grey;'>(significance=0.32)</span>