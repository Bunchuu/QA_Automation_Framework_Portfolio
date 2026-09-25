# QA Automation Framework Portfolio

![Automated Regression Suite](https://github.com/Bunchuu/QA_Automation_Framework_Portfolio/actions/workflows/tests.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.11-blue.svg)
![Playwright](https://img.shields.io/badge/playwright-tested-green.svg)
![Pytest](https://img.shields.io/badge/pytest-ready-brightgreen.svg)
![Code Style: Ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)

Lightweight test automation framework demonstrating API and Web UI test strategies using Python, Playwright, and Pytest, fully integrated with GitHub Actions CI/CD.

---

## Test Scope

* **API Testing (`tests/test_api.py`):**
  * Full CRUD coverage on REST endpoints (GET, POST, PUT, DELETE).
  * Negative test scenarios and contract validation (404 Not Found handling).
  * Response payload and schema assertions.
* **UI Testing (`tests/test_ui.py` + `pages/`):**
  * Implemented using the **Page Object Model (POM)** pattern.
  * Authentication flows: positive login and negative validation scenarios.
  * Asynchronous DOM rendering and explicit timeout handling.
* **Code Quality & Linting:**
  * Static code analysis with **Ruff** ensuring strict compliance with PEP 8 standards.
* **CI/CD Pipeline (`.github/workflows/tests.yml`):**
  * Automated regression pipeline triggered on every `push` and `pull_request` to `main`.
  * Pre-test quality gate executing `ruff check .` for static analysis.
  * Multi-step headless execution on clean Ubuntu Linux runners.
  * Standalone HTML test report generated and uploaded as a build artifact via `actions/upload-artifact`.

---

## Repository Structure

```text
QA_Automation_Framework_Portfolio/
├── .github/
│   └── workflows/
│       └── tests.yml          # GitHub Actions CI pipeline configuration
├── pages/
│   ├── __init__.py
│   ├── dynamic_loading_page.py # Dynamic loading Page Object
│   └── login_page.py          # Authentication Page Object
├── tests/
│   ├── __init__.py
│   ├── test_api.py            # API regression tests (requests)
│   └── test_ui.py             # Web UI regression tests (Playwright)
├── conftest.py                # Shared fixtures and test configuration
├── requirements.txt           # Project dependencies
└── .gitignore                 # Untracked files filter
```

---

## Local Setup

1. **Clone the repository and navigate to root:**
   ```bash
   git clone https://github.com/Bunchuu/QA_Automation_Framework_Portfolio.git
   cd QA_Automation_Framework_Portfolio
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies and browser binaries:**
   ```bash
   pip install -r requirements.txt
   playwright install chromium
   ```

4. **Run code linting:**
   ```bash
   ruff check .
   ```
   
5. **Run the test suite:**
   ```bash
   pytest -v
   ```