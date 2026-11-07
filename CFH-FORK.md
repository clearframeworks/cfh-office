# CFH Office fork

CFH Office is an independent development fork of LibreOffice 26.8.2.2, upstream commit 9dea406ab7695df6325b11b0e19fdca8db4b7276. LibreOffice and its contributors retain their copyrights and trademark rights. This fork is not endorsed by The Document Foundation.

CFH added a build configuration wrapper and original branding assets on 2026-11-07. CFH disabled donation prompts and dispatch, and its build wrapper removes donation menu controls without changing the destination to another party. The wrapper checks all nine configured branding overrides before running upstream configure. This does not establish that every installer, icon, donation surface or other trademark reference has been replaced; distribution requires that review and a verified build.

The upstream license texts and notices remain in the source tree. Source: https://github.com/clearframeworks/cfh-office/tree/cfh-office-26-8-2-2