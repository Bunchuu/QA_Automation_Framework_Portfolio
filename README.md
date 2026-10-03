# QA Automation Framework Portfolio

![Automated Regression Suite](https://github.com/Bunchuu/QA_Automation_Framework_Portfolio/actions/workflows/tests.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.11-blue.svg)
![Playwright](https://img.shields.io/badge/playwright-tested-green.svg)
![Docker](https://img.shields.io/badge/docker-containerized-blue.svg)
![Pytest](https://img.shields.io/badge/pytest-ready-brightgreen.svg)
![Code Style: Ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)

Lightweight test automation framework demonstrating REST API and Web UI test strategies using Python, Playwright, and Pytest, containerized with Docker and fully integrated into a GitHub Actions CI/CD pipeline.

---

## Test Scope

* **API Testing (`tests/test_api.py`):**
  * Full CRUD lifecycle coverage on REST endpoints (GET, POST, PUT, DELETE).
  * Data-driven testing with `@pytest.mark.parametrize` for positive and negative scenarios.
  * Negative test handling across invalid payload structures and non-existent IDs (404 Not Found).
  * Contract verification, schema validation, and collection assertions.
* **UI Testing (`tests/test_ui.py` + `pages/`):**
  * Implemented using the **Page Object Model (POM)** pattern.
  * Parameterized authentication test cases verifying multiple error states and input validations.
  * Dynamic list operations, element state assertions, and live count verifications.
  * Headless browser execution with centralized fixture management (`conftest.py`).
  * Automated failure diagnostics capturing screenshots and Playwright traces on test failure.
* **Code Quality & Linting:**
  * Static code analysis with **Ruff** enforcing PEP 8 standards.
* **CI/CD Pipeline (`.github/workflows/tests.yml`):**
  * Automated regression pipeline triggered on every `push` and `pull_request` to `main`.
  * Multi-step headless test execution on Ubuntu Linux runners.
  * Automated HTML regression report generated and preserved as a build artifact.

---

## Repository Structure

```text
QA_Automation_Framework_Portfolio/
├── .dockerignore              # Docker build exclusions
├── .github/
│   └── workflows/
│       └── tests.yml          # GitHub Actions CI/CD pipeline configuration
├── .gitignore                 # Git ignore rules
├── Dockerfile                 # Containerized test runner environment
├── README.md                  # Project documentation
├── conftest.py                # Centralized pytest fixtures & test setup
├── pages/
│   ├── __init__.py            # Package initialization marker
│   ├── login_page.py          # Authentication Page Object Model
│   └── todo_page.py           # Task management Page Object Model
├── requirements.txt           # Project dependencies
└── tests/
    ├── __init__.py            # Package initialization marker
    ├── test_api.py            # API regression test suite (CRUD & contract validation)
    └── test_ui.py             # Web UI test suite (Playwright POM)
```

---

## Local Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Bunchuu/QA_Automation_Framework_Portfolio.git
   cd QA_Automation_Framework_Portfolio
   ```

2. **Setup virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies and browser binaries:**
   ```bash
   pip install -r requirements.txt
   playwright install chromium
   ```

4. **Run static analysis:**
   ```bash
   ruff check .
   ```
   
5. **Execute tests with HTML report:**
   ```bash
   pytest -v --html=report.html --self-contained-html
   ```

6. **Inspect failure traces (Playwright Trace Viewer):**
   ```bash
   playwright show-trace test-results/trace_<test_name>.zip
   ```

---

## Docker Execution

Run the complete headless test suite in an isolated Linux container:
```bash
docker build -t qa-portfolio-tests .
docker run --rm qa-portfolio-tests
```