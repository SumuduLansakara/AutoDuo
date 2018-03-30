#!/usr/bin/env python3
import logging
import sys

from selenium.common import exceptions

import exercise_page
import home_page
import lesson_page
import logger
import login_page
import player
import translator
from webdriver import WebDriver


def start(user, pwd, repetitions):
    # load translator dictionaries
    translator.train()

    # setup web driver
    webdriver = WebDriver(r'https://www.duolingo.com/')
    webdriver.init_chrome_driver()

    with webdriver:
        # Login Page: login to account
        logging.getLogger().info("logging in")
        login_page.init_page(webdriver)
        login_page.click_signin()
        login_page.type_username(user)
        login_page.type_password(pwd)
        login_page.click_login()

        # Home page: start Basics-1
        logging.getLogger().info("selecting exercise")
        home_page.init_page(webdriver)
        home_page.click_exercise("Basics-1")

        # Exercise page: start lesson 1
        exercise_page.init_page(webdriver)
        exercise_page.init_exercise("Basics-1")

        lesson_page.init_page(webdriver)
        for l in range(1, repetitions + 1):
            logging.getLogger().info("starting lesson {}/{}".format(l, repetitions))
            exercise_page.click_lesson("1")

            challenges = player.do_all_challenges()
            logging.getLogger().debug("{} challenges completed".format(challenges))

            # exercise complete
            while True:
                try:
                    lesson_page.click_next(5)
                except exceptions.TimeoutException:
                    break
            logging.getLogger().info("lesson completed")

        logging.getLogger().info("{} repetitions completed".format(repetitions))


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


def load_cmdline_params():
    index = 1
    cmdline = {}
    while index < len(sys.argv):
        str = sys.argv[index]
        if sys.argv[index].startswith("-"):
            cmdline[str] = sys.argv[index + 1]
            index += 1
        else:
            cmdline[str] = None
        index += 1
    return cmdline


if __name__ == '__main__':
    logger.init_logging(True, True)
    _cmdline = load_cmdline_params()
    logging.debug("commandline: {}".format(_cmdline))
    if "-e" not in _cmdline:
        raise ValueError("Duolingo username/email not provided")
    if "-p" not in _cmdline:
        raise ValueError("Duolingo user password not provided")
    _repetitions = int(_cmdline["-r"]) if "-r" in _cmdline else 5

    start(_cmdline["-e"], _cmdline["-p"], _repetitions)
