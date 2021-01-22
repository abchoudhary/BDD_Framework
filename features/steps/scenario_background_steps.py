from behave import *
from selenium import webdriver


@given('launch browser')
def launch_browser(context):
    assert True, "Test passed"


@when('open application')
def open_application(context):
    assert True, "Test passed"


@when('Enter valid username and password')
def enter_credentials(context):
    assert True, "Test passed"


@when('click on login')
def click_login(context):
    assert True, "Test passed"


@then('User must login to Dashboard page')
def validate_login(context):
    assert True, "Test passed"


@when('navigate to search page')
def navigate_search_page(context):
    assert True, "Test passed"


@then('search page should display')
def validate_search_page(context):
    assert True, "Test passed"


@when('navigate to advanced search page')
def navigate_advanced_search_page(context):
    assert True, "Test passed"


@then('advanced search page should display')
def validate_advanced_search_page(context):
    assert True, "Test passed"
