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





