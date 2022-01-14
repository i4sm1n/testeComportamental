from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

def wait_spinner(driver):
    while (driver.find_element_by_xpath('/html/body/app-root/ng-http-loader').is_displayed()):
        pass

@given('a user with an administrator profile properly logged in version 1.9.12 of the platform #5 and on the Users page')
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

    WebDriverWait(context.driver, 15).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/app-root/app-sidebar-layout/div/nav/div/div[2]/ul[1]/li[3]/a")))

    user_btn = context.driver.find_element_by_xpath("/html/body/app-root/app-sidebar-layout/div/nav/div/div[2]/ul[1]/li[3]/a")
    user_btn.click()

    time.sleep(5)

@when('the user clicks on Add User filling in the necessary data correctly')
def when(context):
   WebDriverWait(context.driver, 15).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/app-root/app-sidebar-layout/div/div/app-administrator/div/app-users/div/div/app-custom-card/div/div[2]/div/div/div[1]/div/a[1]")))

   addUser_btn = context.driver.find_element_by_xpath("/html/body/app-root/app-sidebar-layout/div/div/app-administrator/div/app-users/div/div/app-custom-card/div/div[2]/div/div/div[1]/div/a[1]")
   addUser_btn.click()
   time.sleep(5)

   #excluir usuário manualmente, por enquanto

   name_field = context.driver.find_element_by_id("name")
   name_field.send_keys("Usuário teste")

   phone_field = context.driver.find_element_by_id("phone")
   phone_field.send_keys("85000131415")

   time.sleep(5)

   email_field = context.driver.find_element_by_id("email")
   email_field.send_keys("iasmin1234@hotmail.com")

   wait_spinner(context.driver)

   language_field = Select(context.driver.find_element_by_id("language"))
   language_field.select_by_value("1: Object")
   #no código da página não mostra os item do select de lingua

   time.sleep(5)

   level_field = Select(context.driver.find_element_by_id("profile"))
   level_field.select_by_value("1: Object")

   time.sleep(5)

   country_field = Select(context.driver.find_element_by_id("country"))
   country_field.select_by_value("7: Object")

   time.sleep(5)

   state_field = Select(context.driver.find_element_by_id("state"))
   state_field.select_by_value("2: Object")


   save_btn = context.driver.find_element_by_id("save")
   save_btn.click()

@then('the system returns a notification of the action s success And show the new user in the user list')
def then(context):
    time.sleep(5)

    WebDriverWait(context.driver, 15).until(expected_conditions.text_to_be_present_in_element((By.XPATH, "/html/body/app-root/app-sidebar-layout/div/div/app-alert-system/div/div/div[1]"), "User created!"))

    search_user = context.driver.find_element_by_id("email")
    search_user.send_keys("iasmin1234@hotmail.com")

    search_btn = context.driver.find_element_by_xpath("/html/body/app-root/app-sidebar-layout/div/div/app-administrator/div/app-users/div/div/app-custom-card/div/div[2]/div/div/div[2]/div[1]/app-filter-users/div/div/table/tbody/tr/td[5]/app-filter-actions/div/button[2]")
    search_btn.click()

    WebDriverWait(context.driver, 15).until(expected_conditions.text_to_be_present_in_element((By.XPATH, "/html/body/app-root/app-sidebar-layout/div/div/app-administrator/div/app-users/div/div/app-custom-card/div/div[2]/div/div/div[2]/div[2]/div/table/tbody/tr[1]/td[3]"), "iasmin1234@hotmail.com"))
    context.driver.quit()
#Mudar o email nas linhas 56, 90 e 95 e o numero de telefone na linha 51 manualmente