import logging
import os

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.remote_connection import LOGGER

state_dir = f"{os.getcwd()}/state"
userdata_path = f"{state_dir}/userdata"
url = 'https://www.duolingo.com/'


def get_driver() -> WebDriver:
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-data-dir={userdata_path}")
    options.headless = False
    driver = webdriver.Chrome(executable_path="drivers/chromedriver", options=options)
    driver.implicitly_wait(5)
    return driver


def init_logging():
    LOGGER.setLevel(logging.WARNING)
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)-.1s %(message)s', datefmt='%H:%M:%S')


def start():
    init_logging()
    driver = get_driver()
    driver.get(url)

    root = driver.find_element(By.ID, 'root')

    # TODO: automate user interaction


if __name__ == '__main__':
    start()
