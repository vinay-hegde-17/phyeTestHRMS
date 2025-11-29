import allure
from actions.login_actions import LoginActions

@allure.feature("Login")
@allure.story("HRMS Google Login")
def test_hrms_login(driver, base_url):
    """Test successful login with valid credentials from JSON"""
    login = LoginActions(driver, base_url)
    
    with allure.step("Perform Google Login"):
        assert login.login_to_hrms(), "Login failed!"
