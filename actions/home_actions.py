from pages.home_page import HomePage

class HomeActions:

    def __init__(self, driver):
        self.home_page = HomePage(driver)

    def open_home(self, base_url):
        self.home_page.open_home_page(base_url)

    def verify_logo(self):
        return self.home_page.is_logo_visible()
    
    def get_home_url(self):
        return self.home_page.get_current_url()
