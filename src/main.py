#!/usr/bin/env python3
import sys

from selenium.common import exceptions

import brain
import exercise_page
import home_page
import lesson_page
import login_page
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

    challenges = do_exercise_2()
    print("{} challenges completed".format(challenges))

    # exercise complete
    # TODO: handle exercise completion
    lesson_page.click_next()

    webdriver.close()


def do_exercise_2():
    cid = 0
    prev_header = None
    prev_data = 0
    MAX_LOAD_ATTEMPTS = 10
    while True:
        try:
            challenge_header = lesson_page.get_challenge_header().strip()
            challenge_load_attempts = 0
            while challenge_load_attempts < MAX_LOAD_ATTEMPTS:
                challenge_load_attempts += 1
                if challenge_header:
                    if challenge_header != prev_header:
                        break
                    type_, _ = brain.decide_type_and_data(challenge_header)
                    if type_ == brain.ChallengeType.write_in_english:
                        hint = lesson_page.get_hint_sentence(challenge_load_attempts / 2)
                        hint = translator.sanitize(hint)
                        if hint != prev_data:
                            break
                challenge_header = lesson_page.get_challenge_header().strip()
            else:
                print("### max attempts reached")
                return cid
        except exceptions.StaleElementReferenceException:
            print("### StaleElementReferenceException")
            return cid
        except exceptions.TimeoutException:
            print("### TimeoutException")
            return cid
        except Exception:
            print("### Generic")
            return cid
        cid += 1
        type_, data = brain.decide_type_and_data(challenge_header)
        if type_ == brain.ChallengeType.write_in_english:
            hint = lesson_page.get_hint_sentence()
            hint = translator.sanitize(hint)
            print("challenge {}: {} [{}]".format(cid, challenge_header, hint))
            prev_data = hint
            lesson_page.type_english(translator.g2e(hint))
        else:
            print("challenge {}: {}".format(cid, challenge_header))
            prev_data = data
            if type_ == brain.ChallengeType.write_in_german:
                lesson_page.type_german(translator.e2g(data))
            elif type_ == brain.ChallengeType.select_in_german:
                lesson_page.select_radio(translator.e2g(data))
        lesson_page.click_next()
        lesson_page.click_next()
        lesson_page.wait_till_header_changed(challenge_header, 1)
        prev_header = challenge_header


def do_exercise_1():
    # Lesson page: do challenges
    for i in range(7):
        challenge = lesson_page.get_challenge_header()
        print("challenge {}: {}".format(i + 1, challenge))
        type_, data = brain.decide_type_and_data(challenge)
        if type_ == brain.ChallengeType.write_in_english:
            hint = lesson_page.get_hint_sentence()
            lesson_page.type_english(translator.g2e(hint))
        elif type_ == brain.ChallengeType.write_in_german:
            lesson_page.type_german(translator.e2g(data))
        elif type_ == brain.ChallengeType.select_in_german:
            lesson_page.select_radio(translator.e2g(data))
        lesson_page.click_next()
        lesson_page.click_next()
        lesson_page.wait_till_header_changed(challenge, 1)
        # time.sleep(0.4)


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
