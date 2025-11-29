import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption("--headed", action="store_true", help="Run tests in headed mode")
    parser.addini("base_url", "Base URL for the application under test")

@pytest.fixture
def driver(request):
    headed = request.config.getoption("--headed")

    chrome_options = Options()

    if not headed:
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
    
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36")

    driver = webdriver.Chrome(service=ChromeService(), options=chrome_options)
    driver.maximize_window()
    
    yield driver
    driver.quit()

@pytest.fixture
def base_url(pytestconfig):
    return pytestconfig.getini("base_url")
