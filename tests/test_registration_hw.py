from data.user_data_hw import registration_user_hw, invalid_email_user_hw, invalid_password_user_hw, \
    registered_exists_user_hw, create_user_hw
from pages.registration_page import RegistrationPage


def test_registration_success(driver):
    registration_page = RegistrationPage(driver)
    user_hw = create_user_hw()

    registration_page.open_registration_form()
    registration_page.fill_email(user_hw.username)
    registration_page.fill_password(user_hw.password)
    registration_page.submit_registration()

    assert registration_page.is_registered() is True

def test_registration_with_wrong_email(driver):
    registration_page = RegistrationPage(driver)
    user_hw = invalid_email_user_hw()

    registration_page.open_registration_form()
    registration_page.fill_email(user_hw.username)
    registration_page.fill_password(user_hw.password)
    registration_page.submit_registration()

    assert "Wrong email or password format" in registration_page.get_alert_text()
    registration_page.accept_alert()

def test_registration_with_wrong_password(driver):
    registration_page = RegistrationPage(driver)
    user_hw = invalid_password_user_hw()

    registration_page.open_registration_form()
    registration_page.fill_email(user_hw.username)
    registration_page.fill_password(user_hw.password)
    registration_page.submit_registration()

    assert "Wrong email or password format" in registration_page.get_alert_text()
    registration_page.accept_alert()

def test_registration_exists_user(driver):
    registration_page = RegistrationPage(driver)
    user_hw = registered_exists_user_hw()

    registration_page.open_registration_form()
    registration_page.fill_email(user_hw.username)
    registration_page.fill_password(user_hw.password)
    registration_page.submit_registration()

    assert registration_page.get_alert_text() == "User already exist"
    registration_page.accept_alert()



