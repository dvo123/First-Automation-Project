from utils import conftest as _utils_conftest

# Re-export fixtures from utils.conftest so pytest can discover them when run from the project root
driver = _utils_conftest.driver
