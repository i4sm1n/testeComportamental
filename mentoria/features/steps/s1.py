from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

def wait_spinner(driver):
    while (driver.find_element_by_xpath('/html/body/app-root/ng-http-loader').is_displayed()):
        pass

@given('a user with an administrator profile properly logged in version 1.9.12 of the platform And monitoring a company on the Forum page')
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
#    wait_spinner(context.driver)

    WebDriverWait(context.driver, 15).until(expected_conditions.visibility_of_element_located((By.ID, "name")))

    search_company_field = context.driver.find_element_by_id("name")
    search_company_field.send_keys("aaateste")
    enter_search_btn = context.driver.find_element_by_xpath("/html/body/app-root/app-sidebar-layout/div/div/app-administrator/div/app-list-companies/div/div/app-custom-card/div/div[2]/div/div/div[2]/div[1]/app-filter-companies/div/div/table/tbody/tr/td[5]/app-filter-actions/div/button[2]")
    enter_search_btn.click()

    time.sleep(5)
#    wait_spinner(context.driver)

    monitor_btn = context.driver.find_element_by_xpath("/html/body/app-root/app-sidebar-layout/div/div/app-administrator/div/app-list-companies/div/div/app-custom-card/div/div[2]/div/div/div[2]/div[2]/div/table/tbody/tr[1]/td[1]/a")
    monitor_btn.click()

    time.sleep(5)
#    wait_spinner(context.driver)

    forum_btn = context.driver.find_element_by_id("tabIndexMenuSidebar")
    forum_btn.click()

    time.sleep(5)
#    wait_spinner(context.driver)

@when('the user clicks at + to create a new discussion And duly fill in the required fields')
def when(context):
    createDisc_btn = context.driver.find_element_by_id("create")
    createDisc_btn.click()

    time.sleep(5)
#    wait_spinner(context.driver)

    title_field = context.driver.find_element_by_id("exampleInputEmail1")
    title_field.send_keys("tituloteste")

    description_field = context.driver.find_element_by_xpath("/html/body/app-root/app-sidebar-layout/div/div/app-create-topic/div/app-custom-card/div/div[2]/div/form/app-text-editor/form/div[2]/div[3]/div[2]")
    description_field.send_keys("descriçãoteste")

    createTopic_btn = context.driver.find_element_by_xpath("/html/body/app-root/app-sidebar-layout/div/div/app-create-topic/div/app-custom-card/div/div[2]/div/form/app-text-editor/form/div[3]/button[1]")
    createTopic_btn.click()

    time.sleep(5)
#    wait_spinner(context.driver)

@then('the system adds the new topic to the Forum listing And notifies you that the topic was created successfully')
def then(context):
    search_forum_field = context.driver.find_element_by_xpath("/html/body/app-root/app-sidebar-layout/div/div/app-topics/div/app-custom-card[2]/div/div[2]/div/div[2]/div[1]/input")
    search_forum_field.send_keys("tituloteste")

    search_forum_btn = context.driver.find_element_by_xpath("/html/body/app-root/app-sidebar-layout/div/div/app-topics/div/app-custom-card[2]/div/div[2]/div/div[2]/div[2]/button")
    search_forum_btn.click()

    WebDriverWait(context.driver, 30).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/app-root/app-sidebar-layout/div/div/app-topics/div/app-custom-card[2]/div/div[2]/div/div[4]/div/div[1]/div/button")))

    WebDriverWait(context.driver, 15).until(expected_conditions.text_to_be_present_in_element((By.XPATH, "/html/body/app-root/app-sidebar-layout/div/div/app-alert-system/div/div/div[1]"), "Topic created!"))
    context.driver.quit()