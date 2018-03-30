import json
import logging
import os
import time

import psutil
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.remote_connection import LOGGER
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import settings


def _get_driver_path(driver_name):
    project_root_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    driver_dir = os.path.join(project_root_dir, "drivers")
    return os.path.join(driver_dir, driver_name)


def warn_if_process_running(processes):
    for proc in psutil.process_iter():
        if proc.name() in processes:
            print("Warning! {} is already running".format(proc.name()))
            break


class WebDriver:
    def __init__(self, url):
        self._driver = None
        self._url = url

    def driver(self):
        return self._driver

    def init_chrome_driver(self, headless=False):
        LOGGER.setLevel(logging.WARNING)
        chrome_options = Options()
        if headless:
            chrome_options.add_argument("--headless")
        warn_if_process_running(["chrome", "chromedriver"])
        self._driver = webdriver.Chrome(executable_path=_get_driver_path('chromedriver'),
                                        chrome_options=chrome_options)

    def __enter__(self):
        self.load_page(self._url)
        return self._driver

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        self._driver.quit()

    def load_page(self, url):
        logging.getLogger().info("loading web page: {}".format(url))
        self._driver.get(url)

    def get_element(self, locator, element_id, timeout=settings.explicit_timeout):
        return WebDriverWait(self._driver, timeout).until(
            EC.visibility_of_element_located((locator, element_id)))

    def get_elements(self, locator, element_id, timeout=settings.explicit_timeout):
        return WebDriverWait(self._driver, timeout).until(
            EC.visibility_of_all_elements_located((locator, element_id)))

    def get_clickable_element(self, locator, element_id, timeout=settings.explicit_timeout):
        return WebDriverWait(self._driver, timeout).until(
            EC.element_to_be_clickable((locator, element_id)))

    def _dispatch_key_event(self, name, options):
        options["type"] = name
        body = json.dumps({'cmd': 'Input.dispatchKeyEvent', 'params': options})
        resource = "/session/%s/chromium/send_command" % self._driver.session_id
        url = self._driver.command_executor._url + resource
        self._driver.command_executor._request('POST', url, body)

    def hold_space(self, duration):
        end_time = time.time() + duration
        options = {
            "code": "KeyW",
            "key": " ",
            "text": " ",
            "unmodifiedText": " ",
            "nativeVirtualKeyCode": ord(" "),
            "windowsVirtualKeyCode": ord(" ")
        }

        while True:
            self._dispatch_key_event("rawKeyDown", options)
            self._dispatch_key_event("char", options)

            if time.time() > end_time:
                self._dispatch_key_event("keyUp", options)
                break

            options["autoRepeat"] = True
            time.sleep(0.001)
