import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")     # Required for CI
    chrome_options.add_argument("--no-sandbox")       # Required for GitHub Actions
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(service=ChromeService(), options=chrome_options)
    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addini("base_url", "Base URL for the application under test")

@pytest.fixture
def base_url(pytestconfig):
    return pytestconfig.getini("base_url")
