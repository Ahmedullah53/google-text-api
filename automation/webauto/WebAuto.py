from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import dload
import os

class WebAuto():
    def __init__(self, path_to_driver=''):
        self.__driver = self.load_driver(path_to_driver)

    def get_driver(self):
        return self.__driver

    def hasDriver(self, path):
        return os.path.exists(path)

    def load_driver(self, path):
        if not self.hasDriver(path):
            dload.save_unzip(os.getenv('Driver_URL'))
            path = './chromedriver_win32/chromedriver.exe'
        return webdriver.Chrome(path)

    def wait_for_element_to_be_present(self, locator, wait=10):
        try:
            element = WebDriverWait(self.__driver, wait).until(
                EC.presence_of_all_elements_located(locator)
            )
            return element
        except Exception as e:
            print(e)
            return None

    def wait_for_element_to_be_clickable(self, locator, wait=10):
        try:
            element = WebDriverWait(self.__driver, wait).until(
                EC.element_to_be_clickable(locator)
            )
            return element
        except Exception as e:
            print(e)
            return None

    def wait_for_element_to_be_visible(self, locator, wait=10):
        try:
            element = WebDriverWait(self.__driver, wait).until(
                EC.visibility_of_element_located(locator)
            )
            return element
        except Exception as e:
            print(e)
            return None

    def wait_for_text_to_be_present(self, locator, text, wait=10):
        try:
            element = WebDriverWait(self.__driver, wait).until(
                EC.text_to_be_present_in_element(locator, text)
            )
            return element
        except Exception as e:
            print(e)
            return None

    def sleep(self, wait=10):
        self.__driver.implicitly_wait(wait)