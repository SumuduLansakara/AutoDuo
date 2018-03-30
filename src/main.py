#!/usr/bin/env python3
import sys

import exercise_page
import home_page
import lesson_page
import login_page
import player
import translator
import webdriver


def start(user, pwd):
    # load translator dictionaries
    translator.train()

    # setup web driver
    webdriver.init_chrome_driver()
    webdriver.load_page(r'https://www.duolingo.com/')

    # Login Page: login to account
    login_page.click_signin()
    login_page.type_username(user)
    login_page.type_password(pwd)
    login_page.click_login()

    # Home page: start Basics-1
    home_page.click_exercise("Basics-1")

    # Exercise page: start lesson 1
    exercise_page.init_exercise("Basics-1")
    exercise_page.click_lesson("1")

    challenges = player.do_all_challenges()
    print("{} challenges completed".format(challenges))

    # exercise complete
    # TODO: handle exercise completion
    lesson_page.click_next()

    webdriver.close()


def get_user_credentials():
    index = 1
    user = None
    pwd = None
    while index < len(sys.argv):
        if sys.argv[index] == "-e":
            user = sys.argv[index + 1]
            index += 1
        elif sys.argv[index] == "-p":
            pwd = sys.argv[index + 1]
            index += 1
        index += 1
    if user is None or pwd is None:
        raise ValueError("Duolingo user credentials not provided!")
    return user, pwd


if __name__ == '__main__':
    start(*get_user_credentials())
