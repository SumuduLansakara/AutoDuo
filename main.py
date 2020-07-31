import logging
import os
from typing import Tuple

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.remote_connection import LOGGER

from timed_practice import TimedPractice

state_dir = f"{os.getcwd()}/state"
userdata_path = f"{state_dir}/userdata"
url = 'https://www.duolingo.com/'


def get_driver() -> Tuple[WebDriver, bool]:
    """ returns web-driver and a bool which is False if this is the first run """
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-data-dir={userdata_path}")
    options.headless = False
    is_userdata_found = os.path.isdir(userdata_path)
    driver = webdriver.Chrome(executable_path="drivers/chromedriver", options=options)
    driver.implicitly_wait(5)  # TODO: use explicit waits
    return driver, is_userdata_found


def init_logging():
    LOGGER.setLevel(logging.WARNING)
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)-.1s %(message)s', datefmt='%H:%M:%S')


def start():
    init_logging()
    driver, is_userdata_found = get_driver()
    driver.get(url)
    root = driver.find_element(By.ID, 'root')

    if not is_userdata_found:
        logging.debug("Fresh run")
        _ = root.find_element(By.XPATH, "//a[@data-test='get-started-top']")
        logging.info("You must manually log-in in the first run. You have 60 seconds (rerun if timed-out) !")
        input("press <Enter> after logging in.. ")

    basics = root.find_element(By.XPATH, "//div[contains(text(), 'Basics 1')]")
    parent = basics.find_element(By.XPATH, '..')
    logging.debug("click lesson logo")
    parent.click()

    level_box = root.find_element(By.XPATH, "//div[contains(text(), 'Level')]")
    btn = level_box.find_element(By.XPATH, "//button[@data-test='start-button']")
    logging.debug("click lesson start button")  # FIXME: sometimes this fails
    btn.click()

    start_span = driver.find_element(By.XPATH, "//span[contains(text(), 'Start timed practice')]")
    logging.debug("click start practice button")
    start_span.find_element(By.XPATH, '..').click()

    practice = TimedPractice(driver)
    practice.start()


if __name__ == '__main__':
    start()
