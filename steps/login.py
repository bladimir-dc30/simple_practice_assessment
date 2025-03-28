from behave import *
from pages.login import LoginPage
from selenium import webdriver


@given('I open the web browser')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


@when('I open simple practice website')
def step_impl(context):
    login = LoginPage(context.driver)
    login.open_simple_practice_website()


@when('I type {email} on the email input')
def step_impl(context, email):
    login_page = LoginPage(context.driver)
    login_page.input_email(email)


@when('I type {password} on the password input')
def step_impl(context, password):
    login_page = LoginPage(context.driver)
    login_page.input_password(password)


@when('I click on the sign in button')
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.click_sign_in_btn()


@then('I validate that the simple practice website is displayed correctly')
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.verify_simple_practice_website_is_displayed()


@then('I validate that the simple practice website is not displayed')
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.verify_simple_practice_website_is_not_displayed()


@then('I validate that the required error messages are displyed')
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.verify_required_error_messages_are_displayed()

@then('I quit driver')
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.quit_driver()

