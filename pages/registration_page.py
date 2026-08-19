from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class RegistrationPage:
    REGISTRATION_NAV_LINK = (By.CSS_SELECTOR, "[href='/login']")
    EMAIL_INPUT_R = (By.CSS_SELECTOR, "[name='email']")
    PASSWORD_INPUT_R = (By.CSS_SELECTOR, "input[name='password']")
    REGISTRATION_BTN = (By.XPATH, "//button[text()='Registration']")
    SIGN_OUT_BTN_R = (By.XPATH, "//*[text()='Sign Out']")

    def __init__(self, driver):
        self.driver = driver

    def open_registration_form(self):
        self.driver.find_element(*self.REGISTRATION_NAV_LINK).click()

    def fill_email_r(self, email):
        self.driver.find_element(*self.EMAIL_INPUT_R).clear()
        self.driver.find_element(*self.EMAIL_INPUT_R).send_keys(email)

    def fill_password_r(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT_R).clear()
        self.driver.find_element(*self.PASSWORD_INPUT_R).send_keys(password)

    def submit_registration(self):
        self.driver.find_element(*self.REGISTRATION_BTN).click()

    def is_logged_r(self):
        try:
            # WebDriverWait розпізнає елемент і повертає його. Додатковий .is_displayed() не потрібен.
            return bool(
                WebDriverWait(self.driver, timeout=5).until(
                    EC.visibility_of_element_located(self.SIGN_OUT_BTN_R)
                )
            )
        except TimeoutException:
            return False

    def get_alert_text_r(self):
        alert = WebDriverWait(self.driver, timeout=5).until(
            EC.alert_is_present()
        )
        return alert.text

    def accept_alert_r(self):
        self.driver.switch_to.alert.accept()


























