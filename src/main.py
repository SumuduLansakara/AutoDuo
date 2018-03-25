#!/usr/bin/env python3
import sys

import brain
import settings
import translator
import webdriver
from exercise_page import ExercisePage
from home_page import HomePage
from lesson_page import LessonPage
from login_page import LoginPage


def start(user, pwd):
    # load translator dictionaries
    translator.train()

    # setup web driver
    driver = webdriver.get_chrome_driver()
    driver.implicitly_wait(settings.implicit_timeout)
    driver.get(r'https://www.duolingo.com/')

    # Login page: login to account
    login = LoginPage(driver)
    login.click_signin()
    login.type_username(user)
    login.type_password(pwd)
    login.click_login()

    # Home page: start Basics-1
    home = HomePage(driver)
    home.click_exercise("Basics-1")

    # Exercise page: start lesson 1
    exercise = ExercisePage(driver, "Basics-1")
    exercise.click_lesson("1")

    # Lesson page: do challenges
    lesson = LessonPage(driver)
    for i in range(7):
        challenge = lesson.get_challenge_header()
        print(i, challenge)
        type_, data = brain.decide_type_and_data(challenge)
        if type_ == brain.ChallengeType.write_in_english:
            hint = lesson.get_hint_sentence()
            lesson.type_english(translator.g2e(hint))
        elif type_ == brain.ChallengeType.write_in_german:
            lesson.type_german(translator.e2g(data))
        elif type_ == brain.ChallengeType.select_in_german:
            lesson.select_radio(translator.e2g(data))
        lesson.click_next()
        lesson.click_next()
        lesson.wait_till_header_changed(challenge, 1)
        # time.sleep(0.4)
    # exercise complete
    lesson.click_next()
    driver.quit()


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
