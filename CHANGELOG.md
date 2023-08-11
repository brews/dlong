# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2023-08-11
### Added
- Added `dlong.__version__`.
### Changed
- Check code quality with `ruff check .`. Drop `flake8`.
- Exclude .github from source builds.
- Switch package build system from setuptools to hatchling.
### Fixed
- Minor code smell cleanup in `FractionalDiscount.__eq__`.
- Fixed bad release links in CHANGELOG.

## [0.1.0] - 2022-10-13
 - Initial release.

[0.2.0]: https://github.com/brews/dlong/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/brews/dlong/releases/tag/v0.1.0
