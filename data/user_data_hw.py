from faker import Faker
from models.user_hw import UserHW
fake = Faker()

def create_user_hw(username=None, password=None):
    return UserHW(
        username=username if username is not None else fake.unique.email(),
        password=password if password is not None else fake.password(
            length=15, special_chars=True, digits=True, upper_case=True, lower_case=True
        )
    )
VALID_EMAIL_HW = "anna123456@gmail.com"
VALID_PASSWORD_HW = "Anna123456$"
INVALID_EMAIL_HW = "anna123456gmail"
INVALID_PASSWORD_HW = "Ann12"

def registration_user_hw():
    return create_user_hw(username=VALID_EMAIL_HW, password=VALID_PASSWORD_HW)

def invalid_email_user_hw():
    return create_user_hw(username=INVALID_EMAIL_HW, password=VALID_PASSWORD_HW)

def invalid_password_user_hw():
    return create_user_hw(username=VALID_EMAIL_HW, password=INVALID_PASSWORD_HW)

def registered_exists_user_hw():
    return create_user_hw(username=VALID_EMAIL_HW, password=VALID_PASSWORD_HW)

