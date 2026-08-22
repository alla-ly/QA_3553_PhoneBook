import uuid
import random

from models.user import User
from pages.registration_page import RegistrationPage

def test_registration_success(driver):
    registration_page = RegistrationPage(driver)
    # random_suffix = random.randint(1,1_000_000)
    random_suffix = uuid.uuid4().hex[:8]

    user = User(
        email = f"anna_{random_suffix}@gmail.com",
        password = "Anna123456$"
    )
    registration_page.open_registration_form()
    registration_page.fill_email(user.email)
    registration_page.fill_password(user.password)
    registration_page.submit_registration()

    assert registration_page.is_registered() is True

def test_registration_with_wrong_email(driver):
    registration_page = RegistrationPage(driver)

    user = User(
        email = "annagmail.com",
        password = "Anna123456$"
    )

    registration_page.open_registration_form()
    registration_page.fill_email(user.email)
    registration_page.fill_password(user.password)
    registration_page.submit_registration()

    assert "Wrong email or password format" in registration_page.get_alert_text()
    registration_page.accept_alert()

def test_registration_with_wrong_password(driver):
    registration_page = RegistrationPage(driver)

    user = User(
        email = "anna@gmail.com",
        password = "An12"
    )

    registration_page.open_registration_form()
    registration_page.fill_email(user.email)
    registration_page.fill_password(user.password)
    registration_page.submit_registration()

    assert "Wrong email or password format" in registration_page.get_alert_text()
    registration_page.accept_alert()

def test_registration_existing_user(driver):
    registration_page = RegistrationPage(driver)

    user = User(
        email = "anna123@gmail.com",
        password = "Anna123456$"
    )

    registration_page.open_registration_form()
    registration_page.fill_email(user.email)
    registration_page.fill_password(user.password)
    registration_page.submit_registration()

    assert registration_page.get_alert_text() == "User already exist"
    registration_page.accept_alert()

def test_registered_with_empty_email(driver):
    registration_page = RegistrationPage(driver)

    user = User(
        email = "",
        password = "Anna123456$"
    )
    registration_page.open_registration_form()
    registration_page.fill_email(user.email)
    registration_page.fill_password(user.password)
    registration_page.submit_registration()

    assert "Wrong email or password format" in registration_page.get_alert_text()
    registration_page.accept_alert()