import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def _get_driver_path(driver_name):
    project_root_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    driver_dir = os.path.join(project_root_dir, "drivers")
    return os.path.join(driver_dir, driver_name)


def get_chrome_driver(headless=False):
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless")
    return webdriver.Chrome(executable_path=_get_driver_path('chromedriver'),
                            chrome_options=chrome_options)
