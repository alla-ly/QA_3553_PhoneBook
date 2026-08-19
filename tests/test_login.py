
from pages.login_page import LoginPage

VALID_EMAIL = "margo@gmail.com"
VALID_PASSWORD = "Mmar123456$"
INVALID_EMAIL = "margogmail.com"
INVALID_PASSWORD = ""


def test_login_success(driver):
    login_page = LoginPage(driver)

    login_page.open_login_form()
    login_page.fill_email(VALID_EMAIL)
    login_page.fill_password(VALID_PASSWORD)
    login_page.submit_login()

    assert login_page.is_logged() is True #действительно ли проверяет

def test_login_with_wrong_email(driver):
    login_page = LoginPage(driver)

    login_page.open_login_form()
    login_page.fill_email(INVALID_EMAIL)
    login_page.fill_password(VALID_PASSWORD)
    login_page.submit_login()

    assert login_page.get_alert_text() == "Wrong email or password"
    login_page.accept_alert()


def test_login_with_wrong_password(driver):
    login_page = LoginPage(driver)

    login_page.open_login_form()
    login_page.fill_email(VALID_EMAIL)
    login_page.fill_password(INVALID_PASSWORD)
    login_page.submit_login()

    assert login_page.get_alert_text() == "Wrong email or password"
    login_page.accept_alert()

def test_login_unregister_user(driver):
    login_page = LoginPage(driver)

    login_page.open_login_form()
    login_page.fill_email("anna123456@gmail.com")
    login_page.fill_password("anna123456$")
    login_page.submit_login()

    assert login_page.get_alert_text() == "Wrong email or password"
    login_page.accept_alert()















