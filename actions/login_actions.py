import time
import json
from pathlib import Path
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

class LoginActions:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.page = LoginPage(driver)
        self.base_url = base_url
        
        json_path = Path(__file__).parent.parent / "data" / "test_data.json"
        with open(json_path, 'r') as file:
            data = json.load(file)
        
        credentials = data["login_credentials"]["valid_user"]
        self.email = credentials["email"]
        self.password = credentials["password"]

    def login_to_hrms(self):
        """
        Login to HRMS using Google OAuth
        
        Returns:
            bool: True if login successful, False otherwise
        """
        login_url = f"{self.base_url}/login"
        self.page.driver.get(login_url)
        print(f"Navigating to: {login_url}")
        time.sleep(1)

        self.page.click_login_button()
        time.sleep(2)

        if len(self.page.driver.window_handles) > 1:
            self.page.driver.switch_to.window(self.page.driver.window_handles[-1])
            time.sleep(1)

        self.page.enter_email(self.email)
        self.page.click_email_next()
        time.sleep(2)

        self.page.select_account_if_present(self.email)
        time.sleep(1)

        self.page.enter_password(self.password)
        self.page.click_password_next()
        time.sleep(3)

        self.page.click_consent_buttons_if_any()
        time.sleep(3)

        time.sleep(2)
        try:
            if len(self.page.driver.window_handles) > 1:
                self.page.driver.switch_to.window(self.page.driver.window_handles[0])
            else:
                self.page.driver.switch_to.window(self.page.driver.window_handles[0])
        except Exception as e:
            print(f"Window switch info: {e}")
        
        time.sleep(3)
        
        try:
            current_url = self.driver.current_url
            print(f"Current URL after login: {current_url}")
            
            is_logged_in = "phyelements.com" in current_url and "login" not in current_url
            
            if is_logged_in:
                print("✓ Login successful")
            else:
                print("✗ Login failed - still on login page")
            
            return is_logged_in
            
        except Exception as e:
            print(f"✗ Login verification failed: {str(e)}")
            return False