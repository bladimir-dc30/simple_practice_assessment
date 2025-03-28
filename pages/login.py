from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://account.simplepractice.com/"
        self.email_input = (By.ID, "user_email")
        self.password_input = (By.ID, "user_password")
        self.sign_in_btn = (By.ID, "submitBtn")
        self.user_avatar = (By.ID, "user-avatar")
        self.login_error_msg = (By.XPATH, "//*[contains(text(), \"Couldn't sign in\")]")
        self.required_email_error_msg = (By.ID, "user_email-error")
        self.required_password_error_msg = (By.ID, "user_password-error")

    def open_simple_practice_website(self):
        try:
            self.driver.get(self.url)
        except Exception as e:
            raise Exception(f"Login page - simple practice website not found. --> {e}")

    def input_email(self, email):
        try:
            email_input = self.driver.find_element(*self.email_input)
            email_input.send_keys(email)
        except Exception as e:
            raise Exception(f"Login page - email input field not found. --> {e}")

    def input_password(self, password):
        try:
            password_input = self.driver.find_element(*self.password_input)
            password_input.send_keys(password)
        except Exception as e:
            raise Exception(f"Login page - password input field not found. --> {e}")

    def click_sign_in_btn(self):
        try:
            self.driver.find_element(*self.sign_in_btn).click()
        except Exception as e:
            raise Exception(f"Login page - sign in button not found. --> {e}")

    def verify_simple_practice_website_is_displayed(self):
        try:
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(self.user_avatar))
            assert self.driver.find_element(*self.user_avatar) is not None
        except Exception as e:
            raise Exception(f"Simple Practice Home - simple practice home website is not displayed. --> {e}")

    def verify_simple_practice_website_is_not_displayed(self):
        try:
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(self.login_error_msg))
            assert self.driver.find_element(*self.login_error_msg) is not None
        except Exception as e:
            raise Exception(f"Simple Practice Home - simple practice login error message not displayed. --> {e}")

    def verify_required_error_messages_are_displayed(self):
        try:
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(self.required_email_error_msg))
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(self.required_password_error_msg))
            assert self.driver.find_element(*self.required_email_error_msg) is not None
            assert self.driver.find_element(*self.required_password_error_msg) is not None
        except Exception as e:
            raise Exception(f"Simple Practice Home - required error messages not displayed. --> {e}")

    def quit_driver(self):
        try:
            self.driver.quit()
        except Exception as e:
            raise Exception(f"Commons - driver not quit. --> {e}")


