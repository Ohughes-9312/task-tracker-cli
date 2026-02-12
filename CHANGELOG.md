# Changelog

All notable changes to this project will be documented in this file.

The format is based on Keep a Changelog (https://keepachangelog.com/en/1.1.0/),
and this project adheres to Semantic Versioning (https://semver.org/).

---

## [1.0.0] - 2026-02-12

### Added

- Initial release of the Task Tracker CLI.
- Core task operations:
    - Add tasks
    - List tasks (all, pending, completed)
    - Complete tasks
    - Delete tasks
- JSON-based persistent storage.
- Incremental task ID system.
- Timestamp fields (`created_at`, `completed_at`).
- Color-coded CLI output for improved readability.
- Help menu with command usage.
- Input validation and error handling.
- Project documentation (`README.md`).
- MIT License.
- Development tooling:
    - Black (auto-formatting)
    - isort (import sorting)
    - flake8 (linting)
    - pytest (testing)
- Test suite with initial tests for task creation, completion, and deletion.
- Organized project structure with `tests/` folder.

---

## [Unreleased]

### Planned

- Add task editing functionality.
- Add search/filter by keyword.
- Add priority levels.
- Add due dates.
- Add export/import features.
- Add interactive mode (no command-line arguments needed).
- Add more comprehensive test coverage.