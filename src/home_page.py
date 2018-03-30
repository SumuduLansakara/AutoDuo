from selenium.webdriver.common.by import By

_webdriver = None


def init_page(webdriver):
    global _webdriver
    _webdriver = webdriver


def _get_exercise_css(exercise_name):
    return "a[href='/skill/de/{}']".format(exercise_name)


def click_exercise(exercise_name):
    _webdriver.get_element(By.CSS_SELECTOR, _get_exercise_css(exercise_name)).click()
