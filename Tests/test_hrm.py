import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from Pages.login import ValidationMethods as LoginValidationMethods
from Pages.home import ValidationMethods as HomeValidationMethods
from Locators import locators as lc
from Locators.locators import LoginLocators as LL


# Fixture to set up the WebDriver instance for the session
@pytest.fixture(scope='session')
def driver():
    chromedriver_path = r"C:\Users\shiva\OneDrive\Desktop\chromedriver.exe"
    if not os.path.exists(chromedriver_path):
        raise FileNotFoundError(f"ChromeDriver not found at path: {chromedriver_path}")

    # Add ChromeDriver path to the system PATH
    os.environ["PATH"] += os.pathsep + os.path.dirname(chromedriver_path)

    # Set Chrome options
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    # Initialize the WebDriver service
    service = Service(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()

    # Provide the driver to the tests and quit after the session
    yield driver
    time.sleep(6)  # Wait for a few seconds before quitting the driver
    driver.quit()


# Fixture to initialize the Login page object
@pytest.fixture(scope='session')
def login_page(driver):
    return LoginValidationMethods(driver)


# Fixture to initialize the Home page object
@pytest.fixture(scope='session')
def home_page(driver):
    return HomeValidationMethods(driver)


# Test class containing all test cases
class TestHRM:
    # Test case for validating the forgot password link
    def test_TC_PIM_01(self, login_page):
        url = lc.login_url
        login_page.go_to_page(url)
        result = login_page.forgot_password_link()
        assert result == 'Reset Password link sent successfully'

    # Test case for validating login and verification on the admin page
    def test_TC_PIM_02(self, home_page):
        url = lc.login_url
        home_page.go_to_page(url)
        home_page.login_to_OragneHRM_stat(LL.valid_username, LL.valid_password)
        result_1 = home_page.title_verification()
        result_2 = home_page.validation_on_admin_page()
        assert result_1 == 'OrangeHRM'
        assert result_2 == lc.side_panel

    # Test case for validating the main menu
    def test_TC_PIM_03(self, home_page):
        result = home_page.validate_main_menu()
        assert result == lc.main_menu


# Entry point to run the tests
if __name__ == "__main__":
    pytest.main(["-v", "test_hrm.py"])
