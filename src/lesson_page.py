from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

import settings
import webdriver


def _get_element_css(element, text):
    return "{}[data-test='{}']".format(element, text)


def click_next(timeout=settings.explicit_timeout):
    webdriver.get_clickable_element(By.CSS_SELECTOR, _get_element_css('button', 'player-next'), timeout).click()


def click_skip():
    webdriver.get_clickable_element(By.CSS_SELECTOR, _get_element_css('button', 'player-skip')).click()


def get_challenge_header():
    return webdriver.get_element(By.CSS_SELECTOR, _get_element_css('h1', 'challenge-header')).text


def lam():
    a = get_challenge_header()
    # print(">> [{}]".format(a))
    return a


def wait_till_header_changed(current_header, timeout=1):
    try:
        WebDriverWait(webdriver.driver(), timeout).until(
            # lambda x: get_challenge_header() not in [current_header, ""]
            lambda x: lam() != current_header
        )
    except TimeoutException:
        return


def get_hint_sentence(timeout=settings.explicit_timeout):
    css = _get_element_css('span', 'hint-sentence')
    return webdriver.get_element(By.CSS_SELECTOR, css, timeout).text


def type_english(text):
    _type(_get_element_css('textarea', 'challenge-translate-input'), text)


def type_german(text):
    _type(_get_element_css('input', 'challenge-name-input'), text)


def _type(element_css, text):
    element = webdriver.get_element(By.CSS_SELECTOR, element_css)
    element.click()
    element.send_keys(text)
    webdriver.hold_space(0.01)


def select_radio(selection):
    choices = webdriver.get_elements(By.XPATH, "//h1[@data-test='challenge-header']/../ul/li")
    for li in choices:
        if li.find_element_by_xpath("./label/span[2]").text == selection:
            radio_css = _get_element_css('input', 'player-radio')
            li.find_element_by_css_selector(radio_css).click()
