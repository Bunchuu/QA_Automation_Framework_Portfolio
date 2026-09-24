# QA Automation Framework Portfolio

![Automated Regression Suite](https://github.com/Bunchuu/QA_Automation_Framework_Portfolio/actions/workflows/tests.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.11-blue.svg)
![Playwright](https://img.shields.io/badge/playwright-tested-green.svg)
![Framework](https://img.shields.io/badge/pytest-ready-brightgreen.svg)

Projekt demonstracyjny frameworka testowego w Pythonie:
- Testy regresyjne API (requests)
- Testy UI w architekturze Page Object Model (Playwright)
- Potok CI/CD w GitHub Actions uruchamiany na maszynie wirtualnej Linux

---

## Zakres testów

* **API (`tests/test_api.py`):**
  * Pobieranie i tworzenie zasobów (GET, POST)
  * Aktualizacja i usuwanie danych (PUT, DELETE)
  * Ścieżki negatywne (kody błędów 404 Not Found)
* **UI (`tests/test_ui.py` + POM w `pages/`):**
  * Formularz logowania (scenariusz poprawny oraz błędne dane uwierzytelniające)
  * Asynchroniczne ładowanie elementów DOM i obsługa timeoutów
* **CI/CD (`.github/workflows/tests.yml`):**
  * Automatyczny potok w GitHub Actions odpalający Pytest w trybie headless na czystym systemie Linux

---

## Struktura Katalogów

```text
QA_Automation_Framework_Portfolio/
├── .github/
│   └── workflows/
│       └── tests.yml          # Konfiguracja pipeline CI/CD GitHub Actions
├── pages/
│   ├── __init__.py
│   └── dynamic_loading_page.py # Implementacja wzorca Page Object Model (POM)
├── tests/
│   ├── __init__.py
│   ├── test_api.py            # Testy regresyjne API
│   └── test_ui.py             # Testy interfejsu użytkownika (Playwright)
├── conftest.py                # Konfiguracja i współdzielone zasoby Pytest
├── requirements.txt           # Zależności projektowe
└── .gitignore                 # Ochrona przed śledzeniem plików tymczasowych
```

---

## Uruchomienie Lokalne

1. **Sklonuj repozytorium i wejdź do katalogu:**
   ```bash
   git clone https://github.com/Bunchuu/QA_Automation_Framework_Portfolio.git
   cd QA_Automation_Framework_Portfolio
   ```

2. **Utwórz i aktywuj środowisko wirtualne:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Zainstaluj wymagane pakiety oraz przeglądarki Playwright:**
   ```bash
   pip install -r requirements.txt
   playwright install chromium
   ```

4. **Uruchom pełną suitę testową:**
   ```bash
   pytest -v
   ```