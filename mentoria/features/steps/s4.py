from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

@given('a user with an administrator profile properly logged in version 1.9.12 of the platform #4')
def given(context):
    context.driver = webdriver.Chrome("C:/Users/iasmi/Downloads/chromedriver_win32/chromedriver.exe")
    context.driver.get("https://test.jasgme.com/pt/login")
    context.driver.maximize_window()

    username_field = context.driver.find_element_by_id("login")
    username_field.send_keys("iasmin.santos@dellead.com")

    password_field = context.driver.find_element_by_id("inputPassword")
    password_field.send_keys("1234abcd")

    enter_button = context.driver.find_element_by_id("btnLogin")
    enter_button.click()

    time.sleep(5)

@when('the user clicks the high contrast icon')
def when(context):
    contrast_btn = context.driver.find_element_by_id("bt-autocontraste")
    contrast_btn.click()

    WebDriverWait(context.driver, 10).until(expected_conditions.visibility_of_element_located((By.ID, "bt-autocontraste")))

@then('the system deletes the topic from the Forum listing')
def then(context):
    contrast_anebled_btn = context.driver.find_element_by_id("bt-autocontraste")
#    assertEqual(contrast_anebled_btn.enabled().True)

#como conferir que tudo está com o alto contraste ativado