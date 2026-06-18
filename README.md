Practice drag-and-drop test using Selenium and pytest

Setup (PowerShell on Windows):

1. Create and activate a virtual environment (optional but recommended):

    python -m venv .venv
    .\.venv\Scripts\Activate.ps1

2. Install dependencies:

    pip install -r requirements.txt

3. Run the single test:

    pytest -q tests/test_drag_drop.py -s

Notes:
- The project includes a `driver` fixture in `tests/conftest.py` which starts Chrome. Ensure Chrome is installed and chromedriver is compatible. `webdriver-manager` is listed in `requirements.txt` if you prefer to modify the fixture to use it.
- If you hit issues with the ChromeDriver, either install matching chromedriver on PATH or update `tests/conftest.py` to use webdriver-manager.
