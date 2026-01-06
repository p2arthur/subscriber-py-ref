# algokit-subscriber-python-reference

Minimal Python library whose CI/CD, docs, and release flows are delegated to the reusable workflows in `p2arthur/algokit-shared-config-forked`. Only the project-specific contract (package layout, versioning rules, and tokens) lives here; the heavy lifting is centralized so every repo stays consistent.

## What lives here
- Core package in `src/algokit_subscriber/` with version metadata consumed by `python-semantic-release`.
- Tooling config in `pyproject.toml` for Poetry, pytest/coverage, and semantic-release, plus Sphinx docs config in `docs/` (invoked via `poetry run docs`).
- GitHub Actions callers in `.github/workflows` that forward inputs and secrets to the shared workflows.

## How CI/CD is wired
- `.github/workflows/on-main-merge.yml` calls `p2arthur/algokit-shared-config-forked/.github/workflows/on-merge-main.yml@main` with `project_type: python`. It forwards `BOT_ID`, `BOT_SK`, `NPM_TOKEN`, and `GH_TOKEN` so the shared pipeline can run Python CI and drive semantic-release.
- `.github/workflows/pull-request.yml` reuses `p2arthur/algokit-shared-config/.github/workflows/python-on-pull-request.yml@ci/release-workflow` to run the lightweight Python checks (`python-version: 3.12`, tests enabled).

## Shared workflow quick facts
- `on-merge-main.yml` in the shared repo routes to the Python CI lane (lint/test/docs) and then runs the release composite that executes `python-semantic-release` with the bot token minted from `BOT_ID`/`BOT_SK`. `NPM_TOKEN` is only needed if npm-backed steps run in mixed-language contexts.
- Supporting reusable pieces include the Python CI workflow and release/package actions that expect Poetry-managed dependencies, pytest entrypoints, and semantic-release config defined in `pyproject.toml`.

## Required secrets
- `BOT_ID` / `BOT_SK`: GitHub App credentials used to mint the bot token for releases.
- `GH_TOKEN`: Repo-scoped token used for checkouts/builds.
- `NPM_TOKEN`: Only necessary when npm installs/publishing are exercised by the shared workflows.

## Local scripts
Use `poetry install`, `poetry run pytest`, and `poetry run docs`. These entrypoints mirror what the shared workflows call so local and CI behavior stay aligned.
