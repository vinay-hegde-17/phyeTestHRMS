import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService())
    driver.maximize_window()
    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addini(
        "base_url",
        "Base URL for the application under test"
    )

@pytest.fixture
def base_url(pytestconfig):
    return pytestconfig.getini("base_url")
