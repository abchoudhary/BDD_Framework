from behave import *
from selenium import webdriver


@given('I launch chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome()


@when('I open orangeHRM homepage')
def open_homepage(context):
    context.driver.maximize_window()
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@when('Enter username "{user}" and password "{pwd}"')
def enter_credentials(context, user, pwd):
    context.driver.find_element_by_id("txtUsername").clear()
    context.driver.find_element_by_id("txtUsername").send_keys(user)
    context.driver.find_element_by_id("txtPassword").clear()
    context.driver.find_element_by_id("txtPassword").send_keys(pwd)


@when('click on login button')
def click_login(context):
    context.driver.find_element_by_id("btnLogin").click()


# add try except block to handle invalid parameter scenario
@then('User must successfully login to the Dashboard page')
def validate_login_success(context):
    try:
        text = context.driver.find_element_by_xpath("//h1[normalize-space()='Dashboard']").text
    except:
        context.driver.close()
        assert False, "Test failed due to invalid parameters"

    if text == "Dashboard":
        context.driver.close()
        assert True, "Test passed with valid parameters"
