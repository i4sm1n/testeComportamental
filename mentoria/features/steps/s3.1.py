from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

@given('a user with an administrator profile properly logged in version 1.9.12 of the platform #3 and on the Profile page #2')
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

    profile_btn = context.driver.find_element_by_id("tabIndexMenuSidebar")
    profile_btn.click()

    time.sleep(5)

@when('the user changes the language saving the change #2')
def when(context):
   language_field = Select(context.driver.find_element_by_id("language"))
   language_field.select_by_value("2: Object")

   save_btn = context.driver.find_element_by_id("save")
   save_btn.click()

@then('the system translates the entire platform into the chosen language And it presents a notification of change caused successfully')
def then(context):
    time.sleep(5)

    #conferindo na página de perfil
    WebDriverWait(context.driver, 15).until(expected_conditions.text_to_be_present_in_element((By.XPATH, "/html/body/app-root/app-sidebar-layout/div/div/app-profile/div/div/app-custom-card[2]/div/div[2]/div/app-required-fields/div/span"), "All fields with (*) are required"))

    #conferindo na tela inicial
    company_btn = context.driver.find_element_by_id("tabIndexMenuSidebar")
    company_btn.click()

    time.sleep(5)

    WebDriverWait(context.driver, 15).until(expected_conditions.text_to_be_present_in_element((By.XPATH, "/html/body/app-root/app-sidebar-layout/div/div/app-accessibility-bar/div/nav/div/ul/ul/li[2]/button"), "Log Out"))

    #conferindo na aba de acessibilidade
    WebDriverWait(context.driver, 15).until(expected_conditions.text_to_be_present_in_element((By.XPATH, "/html/body/app-root/app-sidebar-layout/div/div/app-accessibility-bar/div/nav/div/ul/li[2]/a/span[3]"), "Skip to content"))

    WebDriverWait(context.driver, 15).until(expected_conditions.text_to_be_present_in_element((By.XPATH, "/html/body/app-root/app-sidebar-layout/div/div/app-profile/div/div/app-custom-card[1]/div/div[1]/span[1]/span"), "UNDERSTANDING PROFILE"))
    context.driver.quit()
# metodo usado: achar texto em inglês
