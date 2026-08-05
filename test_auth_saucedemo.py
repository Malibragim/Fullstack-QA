from selenium.webdriver.common.by import By
import time
from selenium import webdriver




def test_auth():
    driver = webdriver.Edge()
    driver.get('https://www.saucedemo.com/')
    driver.find_element(By.NAME, 'user-name').send_keys('standard_user')
    time.sleep(2)
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, 'submit-button').click()
    time.sleep(2)
    driver.find_element(By.ID, 'react-burger-menu-btn').click()
    time.sleep(2)
    driver.find_element(By.ID, 'logout_sidebar_link').click()
    time.sleep(2)