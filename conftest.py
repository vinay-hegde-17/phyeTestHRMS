import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

@pytest.fixture(params=["chrome", "firefox", "edge"])
def driver(request):
    browser = request.param

    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService())
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService())
    elif browser == "edge":
        driver = webdriver.Edge(service=EdgeService())
    else:
        raise Exception("Browser not supported")

    driver.maximize_window()
    yield driver
    driver.quit()

# Register custom ini option for base_url (no default hard‑coding)
def pytest_addoption(parser):
    parser.addini(
        "base_url",
        "Base URL for the application under test"
    )

@pytest.fixture
def base_url(pytestconfig):
    return pytestconfig.getini("base_url")
