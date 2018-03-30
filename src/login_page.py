from selenium.webdriver.common.by import By

import webdriver


def click_signin():
    webdriver.get_element(By.ID, 'sign-in-btn').click()


def click_login():
    webdriver.get_element(By.ID, 'login-button').click()


def type_username(username):
    webdriver.get_element(By.ID, 'top_login').send_keys(username)


def type_password(password):
    webdriver.get_element(By.ID, 'top_password').send_keys(password)
