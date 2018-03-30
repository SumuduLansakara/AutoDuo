from selenium.webdriver.common.by import By

import webdriver

_href_prefix = None


def init_exercise(exercise_name):
    global _href_prefix
    _href_prefix = "/skill/de/{}".format(exercise_name)


def _get_lesson_css(lesson_name):
    return "a[href='{}/{}']".format(_href_prefix, lesson_name)


def click_lesson(lesson_name):
    webdriver.get_element(By.CSS_SELECTOR, _get_lesson_css(lesson_name)).click()
