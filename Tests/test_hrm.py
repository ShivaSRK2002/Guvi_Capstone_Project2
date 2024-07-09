import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Pages.login import ValidationMethods as LoginValidationMethods
from Pages.home import ValidationMethods as HomeValidationMethods
from Locators import locators as lc
from Locators.locators import LoginLocators as LL


@pytest.fixture(scope='session')
def driver():
    chromedriver_path = r"C:\Users\shiva\OneDrive\Desktop\chromedriver.exe"
    if not os.path.exists(chromedriver_path):
        raise FileNotFoundError(f"ChromeDriver not found at path: {chromedriver_path}")
    os.environ["PATH"] += os.pathsep + os.path.dirname(chromedriver_path)

    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    service = Service(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()

    yield driver
    time.sleep(6)
    driver.quit()


@pytest.fixture(scope='session')
def login_page(driver):
    return LoginValidationMethods(driver)


@pytest.fixture(scope='session')
def home_page(driver):
    return HomeValidationMethods(driver)


class TestHRM:
    def test_TC_PIM_01(self, login_page):
        url = lc.login_url
        login_page.go_to_page(url)
        result = login_page.forgot_password_link()
        assert result == 'Reset Password link sent successfully'

    def test_TC_PIM_02(self, home_page):
        url = lc.login_url
        home_page.go_to_page(url)
        home_page.login_to_OragneHRM_stat(LL.valid_username, LL.valid_password)
        result_1 = home_page.title_verification()
        result_2 = home_page.validation_on_admin_page()
        assert result_1 == 'OrangeHRM'
        assert result_2 == lc.side_panel

    def test_TC_PIM_03(self, home_page):
        result = home_page.validate_main_menu()
        assert result == lc.main_menu


if __name__ == "__main__":
    pytest.main(["-v", "test_hrm.py"])
