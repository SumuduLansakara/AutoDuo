from selenium.webdriver.common.by import By

import webdriver


def _get_exercise_css(exercise_name):
    return "a[href='/skill/de/{}']".format(exercise_name)


def click_exercise(exercise_name):
    webdriver.get_element(By.CSS_SELECTOR, _get_exercise_css(exercise_name)).click()
