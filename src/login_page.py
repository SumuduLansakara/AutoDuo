from selenium.webdriver.common.by import By

_webdriver = None


def init_page(webdriver):
    global _webdriver
    _webdriver = webdriver


def click_signin():
    _webdriver.get_element(By.ID, 'sign-in-btn').click()


def click_login():
    _webdriver.get_element(By.ID, 'login-button').click()


def type_username(username):
    _webdriver.get_element(By.ID, 'top_login').send_keys(username)


def type_password(password):
    _webdriver.get_element(By.ID, 'top_password').send_keys(password)
