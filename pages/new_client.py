import time
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import unittest


class NewClient:
    def __init__(self, driver):
        self.driver = driver
        self.create_btn = (By.CSS_SELECTOR, ".icon-plus")
        self.create_client_btn = (By.XPATH, "(//*[div[@id=\"ember-basic-dropdown-content-ember8\"]]//div//div)[1]")
        self.first_name_input = (By.CSS_SELECTOR, "[name='firstName']")
        self.last_name_input = (By.CSS_SELECTOR, "[name='lastName']")
        self.continue_btn = (By.CSS_SELECTOR, ".footer [type].button")
        self.clients_btn = (By.CSS_SELECTOR, "[aria-label='Clients']")
        self.search_clients_input = (By.CSS_SELECTOR, "[name='utility-search']")
        self.new_client_added = (By.XPATH, "(//*[a[@class=\"ember-view record-name\"]])[1]")
        self.client = None
        self.first_name_error_msg = (
        By.CSS_SELECTOR, "div:nth-of-type(1) > .field > .Ad2MY.ember-view.invalid.validated-input  .error")
        self.last_name_error_msg = (
        By.CSS_SELECTOR, "div:nth-of-type(2) > .field > .Ad2MY.ember-view.invalid.validated-input  .error")
        self.nickname_input = (By.CSS_SELECTOR, "[name='nickname']")
        self.month_input = (By.CSS_SELECTOR, "[name='month']")
        self.day_input = (By.CSS_SELECTOR, "[name='day']")
        self.year_input = (By.CSS_SELECTOR, "[name='year']")
        self.referred_input = (By.CSS_SELECTOR, ".typeahead-trigger-container div")
        self.create_new_referral_btn = (By.CSS_SELECTOR, ".select-box__option [type]")
        self.referred_by_input = (By.CSS_SELECTOR, "input[name='referredBy']")
        self.add_email_btn = (By.CSS_SELECTOR, ".kV73R [type]")
        self.add_email_input = (By.CSS_SELECTOR, ".Ad2MY.ember-view.validated-input > input[name='email']")
        self.add_phone_btn = (By.CSS_SELECTOR, ".xRZu7 > [type]")
        self.add_phone_input = (By.CSS_SELECTOR, "[name='phone']")

    def click_on_the_create_btn(self):
        try:
            self.driver.find_element(*self.create_btn).click()
        except Exception as e:
            raise Exception(f"Simple practice website - create button not found. --> {e}")

    def click_on_the_create_client_btn(self):
        try:
            WebDriverWait(self.driver, 2).until(ec.element_to_be_clickable(self.create_client_btn))
            self.driver.find_element(*self.create_client_btn).click()
        except Exception as e:
            raise Exception(f"Simple practice website - create client button not found. --> {e}")

    def assert_new_client_modal(self):
        try:
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(self.first_name_input))
            assert self.driver.find_element(*self.first_name_input) is not None
        except Exception as e:
            raise Exception(f"Simple Practice Home - new client modal not displayed. --> {e}")

    def input_first_name(self, first_name):
        try:
            WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(self.first_name_input))
            first_name_input = self.driver.find_element(*self.first_name_input)
            first_name_input.send_keys(first_name)
        except Exception as e:
            raise Exception(f"Simple practice home - first name input not found. --> {e}")

    def input_last_name(self, last_name):
        try:
            WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(self.last_name_input))
            last_name_input = self.driver.find_element(*self.last_name_input)
            last_name_input.send_keys(last_name)
        except Exception as e:
            raise Exception(f"Simple practice home - last name input not found. --> {e}")

    def click_on_the_continue_btn(self):
        try:
            WebDriverWait(self.driver, 2).until((ec.element_to_be_clickable(self.continue_btn)))
            continue_btn = self.driver.find_element(*self.continue_btn)
            continue_btn.click()
        except Exception as e:
            raise Exception(f"Simple practice home - continue button not found. --> {e}")

    def click_on_the_clients_btn(self):
        try:
            WebDriverWait(self.driver, 2).until((ec.element_to_be_clickable(self.clients_btn)))
            clients_btn = self.driver.find_element(*self.clients_btn)
            clients_btn.click()
        except Exception as e:
            raise Exception(f"Simple practice home - clients button not found. --> {e}")

    def input_search_client(self, search_client):
        try:
            WebDriverWait(self.driver, 2).until((ec.element_to_be_clickable(self.search_clients_input)))
            search_clients_input = self.driver.find_element(*self.search_clients_input)
            search_clients_input.send_keys(search_client)
            self.client = search_clients_input.text
        except Exception as e:
            raise Exception(f"Simple practice home - search clients input not found. --> {e}")

    def assert_new_client_displayed(self):
        try:
            expected_result = "jose perez"
            WebDriverWait(self.driver, 5).until(
                ec.text_to_be_present_in_element(self.new_client_added, expected_result))
            new_client_added = self.driver.find_element(*self.new_client_added).text
            assert new_client_added == expected_result
        except Exception as e:
            raise Exception(f"Simple Practice Home - new client added not displayed. --> {e}")

    def assert_last_name_error_msg(self):
        try:
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(self.last_name_error_msg))
            assert self.driver.find_element(*self.last_name_error_msg) is not None
        except Exception as e:
            raise Exception(f"Simple Practice Home - last name error message not displayed. --> {e}")

    def assert_first_name_error_msg(self):
        try:
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(self.first_name_error_msg))
            assert self.driver.find_element(*self.first_name_error_msg) is not None
        except Exception as e:
            raise Exception(f"Simple Practice Home - first name error message not displayed. --> {e}")

    def input_nick_name(self, nickname):
        try:
            WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(self.nickname_input))
            nickname_input = self.driver.find_element(*self.nickname_input)
            nickname_input.send_keys(nickname)
        except Exception as e:
            raise Exception(f"Simple practice home - nickname input not found. --> {e}")

    def input_month(self, month):
        try:
            WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(self.month_input))
            input_month = self.driver.find_element(*self.month_input)
            input_month.click()
            self.driver.find_element(By.CSS_SELECTOR, f"[value=\'{month}\']").click()
        except Exception as e:
            raise Exception(f"Simple practice home - month input not found. --> {e}")

    def input_day(self, day):
        try:
            WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(self.day_input))
            input_day = self.driver.find_element(*self.day_input)
            input_day.click()
            self.driver.find_element(By.CSS_SELECTOR, f"[value=\'{day}\']").click()
        except Exception as e:
            raise Exception(f"Simple practice home - day input not found. --> {e}")

    def input_year(self, year):
        try:
            WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(self.year_input))
            input_year = self.driver.find_element(*self.year_input)
            input_year.click()
            self.driver.find_element(By.CSS_SELECTOR, f"[value=\'{year}\']").click()
        except Exception as e:
            raise Exception(f"Simple practice home - year input not found. --> {e}")

    def input_add_email(self, add_email):
        try:
            add_email_btn = self.driver.find_element(*self.add_email_btn)
            self.driver.execute_script("arguments[0].scrollIntoView();", add_email_btn)
            add_email_btn.click()
            WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(self.add_email_input))
            add_email_input = self.driver.find_element(*self.add_email_input)
            add_email_input.send_keys(add_email)
        except Exception as e:
            raise Exception(f"Simple practice home - add email input not found. --> {e}")

    def input_add_phone(self, add_phone):
        try:
            add_phone_btn = self.driver.find_element(*self.add_phone_btn)
            self.driver.execute_script("arguments[0].scrollIntoView();", add_phone_btn)
            add_phone_btn.click()
            WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(self.add_phone_input))
            add_phone_input = self.driver.find_element(*self.add_phone_input)
            add_phone_input.send_keys(add_phone)
        except Exception as e:
            raise Exception(f"Simple practice home - add phone input not found. --> {e}")



