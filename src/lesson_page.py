from selenium.common.exceptions import TimeoutException

import keyboard_helper
from selenium.webdriver.support.ui import WebDriverWait

import settings


class LessonPage:
    def __init__(self, driver):
        self._driver = driver

    def _get_element_css(self, element, text):
        return "{}[data-test='{}']".format(element, text)

    def click_next(self):
        skip_css = self._get_element_css('button', 'player-next')
        self._driver.find_element_by_css_selector(skip_css).click()

    def click_skip(self):
        skip_css = self._get_element_css('button', 'player-skip')
        self._driver.find_element_by_css_selector(skip_css).click()

    def get_challenge_header(self):
        header_css = self._get_element_css('h1', 'challenge-header')
        return self._driver.find_element_by_css_selector(header_css).text

    def wait_till_header_changed(self, current_header, timeout=1):
        try:
            WebDriverWait(self._driver, timeout).until(
                lambda x: self.get_challenge_header() != current_header
            )
        except TimeoutException:
            return

    def get_hint_sentence(self):
        hint_css = self._get_element_css('span', 'hint-sentence')
        return self._driver.find_element_by_css_selector(hint_css).text

    def type_english(self, text):
        print("type english:", text)
        txtarea_css = self._get_element_css('textarea', 'challenge-translate-input')
        self._type(txtarea_css, text)

    def type_german(self, text):
        print("type german:", text)
        input_css = self._get_element_css('input', 'challenge-name-input')
        self._type(input_css, text)

    def _type(self, element_css, text):
        element = self._driver.find_element_by_css_selector(element_css)
        element.click()
        element.send_keys(text)
        keyboard_helper.hold_space(self._driver, 0.01)

    def select_radio(self, selection):
        print("select radio:", selection)
        choices = self._driver.find_elements_by_xpath("//h1[@data-test='challenge-header']/../ul/li")
        for li in choices:
            if li.find_element_by_xpath("./label/span[2]").text == selection:
                radio_css = self._get_element_css('input', 'player-radio')
                li.find_element_by_css_selector(radio_css).click()
