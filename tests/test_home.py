import allure
from actions.home_actions import HomeActions

@allure.feature("Home Page")
@allure.story("Verify Company Logo")
def test_verify_home_logo(driver, base_url):
    actions = HomeActions(driver)

    # Step 1: Open home page
    with allure.step("Open home page"):
        actions.open_home(base_url)

    # Step 2: Verify logo image is present
    with allure.step("Verify logo is visible"):
        assert actions.verify_logo(), "Logo is NOT visible on homepage!"

@allure.feature("Home Page")
@allure.story("Validate Home Page URL")
def test_homepage_url(driver, base_url):

    actions = HomeActions(driver)

    with allure.step("Open Home Page"):
        actions.open_home(base_url)

    with allure.step("Validate correct home URL is loaded"):
        expected_url = "http://www.phyelements.com/"
        current_url = actions.get_home_url()

        assert current_url == expected_url, f"Expected {expected_url}, but got {current_url}"
        