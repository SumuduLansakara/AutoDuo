import difflib
import logging
import time

from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from translator import to_german, to_english


class TimedPractice:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def do_once(self):
        try:
            header = self.driver.find_element(By.XPATH, "//h1[@data-test='challenge-header']")
        except NoSuchElementException:
            self.player_next()
            return
        logging.info(f"header: {header.text}")
        if header.text == 'Mark the correct meaning':
            self.mark_meaning(header)
        elif header.text == 'Tap what you hear':
            self.player_skip()
        elif header.text == 'Write this in German':
            self.write_in_german()
        elif header.text == 'Write this in English':
            self.write_in_english()
        else:
            self.player_skip()

    def start(self):
        i = 0
        while True:
            i += 1
            logging.info(f"round {i}")
            try:
                self.do_once()
            except ElementNotInteractableException:
                self.player_next()
                try:
                    end_carousel = self.driver.find_element(By.XPATH, "//div[@data-test='player-end-carousel']")
                    if end_carousel:
                        self.player_next()
                        logging.info("practice complete")
                        break
                except:
                    pass
            time.sleep(1)

    def write_in_english(self):
        logging.debug("start write in english")
        question = self.driver.find_element(By.XPATH, "//span[@data-test='hint-sentence']").text.lower().strip()
        logging.debug(f"question: [{question}]")
        result = to_english(question)
        logging.debug(f"translation: [{result}]")
        if result:
            answer_area = self.driver.find_element(By.XPATH, "//textarea[@data-test='challenge-translate-input']")
            answer_area.send_keys(result)
            self.player_next()
        else:
            self.player_skip()

        self.player_next()

    def write_in_german(self):
        logging.debug("start write in German")
        question = self.driver.find_element(By.XPATH, "//span[@data-test='hint-sentence']").text.lower().strip()
        logging.debug(f"question: [{question}]")
        result = to_german(question)
        logging.debug(f"translation: [{result}]")
        if result:
            answer_area = self.driver.find_element(By.XPATH, "//textarea[@data-test='challenge-translate-input']")
            answer_area.send_keys(result[0])
            self.player_next()
        else:
            self.player_skip()

        self.player_next()

    def mark_meaning(self, header: WebElement):
        logging.debug("start mark the correct meaning")
        next_div = header.find_element(By.XPATH, '../following::div')
        question = next_div.find_element(By.XPATH, "./div").text.lower().strip()
        answers = to_german(question)
        logging.debug(f"question: {question}, answers: {answers}")

        option_blocks = next_div.find_elements(By.XPATH, ".//label[@data-test='challenge-choice']")
        for opt in option_blocks:
            phrase = opt.find_element(By.XPATH, "./div[@data-test='challenge-judge-text']").text.lower().strip()
            matches = difflib.get_close_matches(phrase, answers)
            if phrase == matches[0]:
                logging.debug(f"translation success")
                input_element = opt.find_element(By.XPATH, './span')
                input_element.click()
                self.player_next()
                break
        else:
            logging.debug(f"translation failed")
            self.player_skip()

        self.player_next()

    def player_skip(self):
        logging.warning("click skip button")
        skip_btn = self.driver.find_element(By.XPATH, "//button[@data-test='player-skip']")
        skip_btn.click()
        self.player_next()

    def player_next(self):
        logging.debug("click next button")
        next_btn = self.driver.find_element(By.XPATH, "//button[@data-test='player-next']")
        next_btn.click()
