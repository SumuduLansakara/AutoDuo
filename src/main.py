#!/usr/bin/env python3

import time

import brain
import translator
import settings
import webdriver
from exercise_page import ExercisePage
from home_page import HomePage
from lesson_page import LessonPage
from login_page import LoginPage


def start():
    # load translator dictionaries
    translator.train()

    # setup web driver
    driver = webdriver.get_chrome_driver()
    driver.implicitly_wait(settings.implicit_timeout)
    driver.get(r'https://www.duolingo.com/')

    # Login page: login to account
    login = LoginPage(driver)
    login.click_signin()
    login.type_username(settings.email)
    login.type_password(settings.password)
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


if __name__ == '__main__':
    start()
