import time
import json
from pathlib import Path
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
        try:
            login_url = f"{self.base_url}/login"
            self.page.driver.get(login_url)
            print(f"Navigating to: {login_url}")
            time.sleep(2)

            print("Step 1: Clicking login button...")
            self.page.click_login_button()
            time.sleep(3)

            print(f"Step 2: Window handles count: {len(self.page.driver.window_handles)}")
            if len(self.page.driver.window_handles) > 1:
                print("Switching to popup window...")
                self.page.driver.switch_to.window(self.page.driver.window_handles[-1])
                time.sleep(2)

            print(f"Step 3: Entering email: {self.email}")
            self.page.enter_email(self.email)
            self.page.click_email_next()
            time.sleep(3)

            print("Step 4: Checking for account selection...")
            self.page.select_account_if_present(self.email)
            time.sleep(2)

            print("Step 5: Entering password...")
            self.page.enter_password(self.password)
            self.page.click_password_next()
            time.sleep(4)

            print("Step 6: Handling consent screens...")
            self.page.click_consent_buttons_if_any()
            time.sleep(4)

            print("Step 7: Switching back to main window...")
            time.sleep(3)
            
            all_handles = self.page.driver.window_handles
            print(f"Total window handles: {len(all_handles)}")
            
            main_window = all_handles[0]
            self.page.driver.switch_to.window(main_window)
            print(f"Switched to main window: {main_window}")
            
            time.sleep(2)
            if len(self.page.driver.window_handles) > 1:
                print("Closing popup windows...")
                for handle in self.page.driver.window_handles[1:]:
                    try:
                        self.page.driver.switch_to.window(handle)
                        self.page.driver.close()
                        print(f"Closed popup window: {handle}")
                    except:
                        pass
                self.page.driver.switch_to.window(main_window)
            
            print(f"Final window handles count: {len(self.page.driver.window_handles)}")
            time.sleep(3)
            
            current_url = self.driver.current_url
            print(f"Final URL: {current_url}")
            print(f"Page title: {self.driver.title}")
            
            is_logged_in = "phyelements.com" in current_url and "login" not in current_url
            
            if is_logged_in:
                print("✓ Login successful")
            else:
                print("✗ Login failed - still on login page")
                self.driver.save_screenshot("login_failed.png")
                print(f"Page source preview: {self.driver.page_source[:500]}")
            
            return is_logged_in
            
        except Exception as e:
            print(f"✗ Login process failed with error: {str(e)}")
            import traceback
            traceback.print_exc()
            try:
                self.driver.save_screenshot("login_error.png")
            except:
                pass
            return False
