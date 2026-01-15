# AlgoKit Subscriber Python Reference

This repository is a thin Python wrapper that delegates CI/CD orchestration to
`algokit-shared-config` while maintaining the contract-based layout expected by
shared workflows.

## Contents
- Core package lives in `src/algokit_subscriber/` with version metadata for semantic-release.
- Tests in `tests/` keep the footprint minimal while verifying the package exports.
- Documentation can be built with `poetry run docs`, producing HTML in `docs/_build/html`.
