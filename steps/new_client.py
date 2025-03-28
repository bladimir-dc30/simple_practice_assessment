from behave import *
from pages.new_client import NewClient


@then(u'I click on the create button')
def step_impl(context):
    new_client = NewClient(context.driver)
    new_client.click_on_the_create_btn()


@then(u'I click on the create client button')
def step_impl(context):
    new_client = NewClient(context.driver)
    new_client.click_on_the_create_client_btn()


@then('I verify that the create client modal is displayed correctly')
def step_impl(context):
    new_client = NewClient(context.driver)
    new_client.assert_new_client_modal()


@then(u'I type {first_name} on the first name input')
def step_impl(context, first_name):
    new_client = NewClient(context.driver)
    new_client.input_first_name(first_name)


@then(u'I type {last_name} on the last name input')
def step_impl(context,last_name):
    new_client = NewClient(context.driver)
    new_client.input_last_name(last_name)


@then('I click on the continue button')
def step_impl(context):
    new_client = NewClient(context.driver)
    new_client.click_on_the_continue_btn()


@then('I click on the clients button')
def step_impl(context):
    new_client = NewClient(context.driver)
    new_client.click_on_the_clients_btn()


@then('I type {search_client} on the search input')
def step_impl(context, search_client):
    new_client = NewClient(context.driver)
    new_client.input_search_client(search_client)


@then('I validate that the client is displayed correctly')
def step_impl(context):
    new_client = NewClient(context.driver)
    new_client.assert_new_client_displayed()


@then('I validat that the last name error message is displayed correctly')
def step_impl(context):
    new_client = NewClient(context.driver)
    new_client.assert_last_name_error_msg()


@then('I validat that the first name error message is displayed correctly')
def step_impl(context):
    new_client = NewClient(context.driver)
    new_client.assert_first_name_error_msg()


@then('I type {nickname} on the nickname input')
def step_impl(context, nickname):
    new_client = NewClient(context.driver)
    new_client.input_nick_name(nickname)


@then(u'I select {month} on the month input')
def step_impl(context, month):
    new_client = NewClient(context.driver)
    new_client.input_month(month)


@then(u'I select {day} on the day input')
def step_impl(context, day):
    new_client = NewClient(context.driver)
    new_client.input_day(day)


@then(u'I select {year} on the year input')
def step_impl(context, year):
    new_client = NewClient(context.driver)
    new_client.input_year(year)


@then('I type {add_email} on the add email input')
def step_impl(context, add_email):
    new_client = NewClient(context.driver)
    new_client.input_add_email(add_email)


@then(u'I type {add_phone} on the add phone input')
def step_impl(context, add_phone):
    new_client = NewClient(context.driver)
    new_client.input_add_phone(add_phone)


