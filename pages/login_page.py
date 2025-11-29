from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.login_locators import LoginLocators

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(self.driver, 15)

    def click_login_button(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, LoginLocators.CLICK_LOGIN_BTN))).click()

    def enter_email(self, email):
        self.wait.until(EC.presence_of_element_located((By.XPATH, LoginLocators.GOOGLE_EMAIL_FIELD))).clear()
        self.wait.until(EC.presence_of_element_located((By.XPATH, LoginLocators.GOOGLE_EMAIL_FIELD))).send_keys(email)

    def click_email_next(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, LoginLocators.GOOGLE_EMAIL_NEXT))).click()
        except:
            self.safe_click(LoginLocators.GOOGLE_EMAIL_NEXT)

    def select_account_if_present(self, email):
        xpath = LoginLocators.ACCOUNT_SELECT.format(email=email)
        return self.safe_click(xpath)

    def enter_password(self, password):
        self.wait.until(EC.presence_of_element_located((By.XPATH, LoginLocators.GOOGLE_PASSWORD_FIELD))).clear()
        self.wait.until(EC.presence_of_element_located((By.XPATH, LoginLocators.GOOGLE_PASSWORD_FIELD))).send_keys(password)

    def click_password_next(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, LoginLocators.GOOGLE_PASSWORD_NEXT))).click()
        except:
            self.safe_click(LoginLocators.GOOGLE_PASSWORD_NEXT)

    def click_consent_buttons_if_any(self):
        for xpath in LoginLocators.CONSENT_BUTTONS:
            if self.safe_click(xpath):
                return True
        return False

    def safe_click(self, locator):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator))).click()
            return True
        except:
            return False
