import pytest
from selenium import webdriver

from data.user_data import exiting_user
from pages.login_page import LoginPage
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--lang=en-US")
    options.add_experimental_option("prefs", {"intl.accept_languages": "en-US,en"})

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://telranedu.web.app/")

    yield driver

    driver.quit()

@pytest.fixture
def authenticated_driver(driver):
    login_page = LoginPage(driver)
    user = exiting_user()

    login_page.open_login_form()
    login_page.fill_email(user.username)
    login_page.fill_password(user.password)
    login_page.submit_login()

    return driver

























