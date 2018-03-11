#!/usr/bin/env python3

import translator
import user
import webdriver
from home_page import HomePage
from login_page import LoginPage


def start():
    # load translator dictionaries
    translator.train()

    # setup web driver
    driver = webdriver.get_chrome_driver()
    driver.implicitly_wait(10)
    driver.get(r'https://www.duolingo.com/')

    # Login page: login to account
    login = LoginPage(driver)
    login.click_signin()
    login.type_username(user.email)
    login.type_password(user.password)
    login.click_login()

    # Home page: start Basics-1
    home = HomePage(driver)
    home.click_exercise("Basics-1")

    input("press any key to exit...")
    driver.quit()


if __name__ == '__main__':
    start()
