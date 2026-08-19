from pages.registration_page import RegistrationPage

VALID_EMAIL = "anna123456@gmail.com"
VALID_PASSWORD = "Anna123456$"
INVALID_EMAIL = "anna123456gmail"
INVALID_PASSWORD = ""
VALID_PASSWORD_KNOW = "Olga12345!"


def test_registration_success(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open_registration_form()
    registration_page.fill_email_r(VALID_EMAIL)
    registration_page.fill_password_r(VALID_PASSWORD)
    registration_page.submit_registration()

    assert registration_page.is_logged_r() is True

def test_registration_with_wrong_email(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open_registration_form()
    registration_page.fill_email_r(INVALID_EMAIL)
    registration_page.fill_password_r(VALID_PASSWORD)
    registration_page.submit_registration()

    assert "Wrong email or password format" in registration_page.get_alert_text_r()
    registration_page.accept_alert_r()

def test_registration_with_wrong_password(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open_registration_form()
    registration_page.fill_email_r(VALID_EMAIL)
    registration_page.fill_password_r(INVALID_PASSWORD)
    registration_page.submit_registration()

    assert "Wrong email or password format" in registration_page.get_alert_text_r()
    registration_page.accept_alert_r()

def test_unregistered_with_same_data(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open_registration_form()
    registration_page.fill_email_r(VALID_EMAIL)
    registration_page.fill_password_r(VALID_PASSWORD)
    registration_page.submit_registration()

    assert registration_page.get_alert_text_r() == "User already exist"
    registration_page.accept_alert_r()

def test_unregistered_with_same_email(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open_registration_form()
    registration_page.fill_email_r(VALID_EMAIL)
    registration_page.fill_password_r(VALID_PASSWORD_KNOW)
    registration_page.submit_registration()

    assert registration_page.get_alert_text_r() == "User already exist"
    registration_page.accept_alert_r()

