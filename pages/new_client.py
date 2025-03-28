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
        self.continue_btn = (By.CSS_SELECTOR, ".ember-view.show.side-flyout.side-flyout-module_component__D3FTo .button.primary")
        self.clients_btn = (By.CSS_SELECTOR, "[aria-label='Clients']")
        self.search_clients_input = (By.CSS_SELECTOR, "[name='utility-search']")
        self.new_client_added = (By.XPATH, "(//*[a[@class=\"ember-view record-name\"]])[1]")
        self.client = None

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
            WebDriverWait(self.driver, 5).until(ec.text_to_be_present_in_element(self.new_client_added, expected_result))
            new_client_added = self.driver.find_element(*self.new_client_added).text
            assert new_client_added == expected_result
        except Exception as e:
            raise Exception(f"Simple Practice Home - new client added not displayed. --> {e}")




