from pages.base_page import BasePage
from locators.home_locators import HomeLocators

class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def open_home_page(self, base_url):
        self.driver.get(base_url)

    def is_logo_visible(self):
        return self.is_visible(HomeLocators.LOGO_IMG)
    
    def get_current_url(self):
        return self.driver.current_url