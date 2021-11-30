from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import dload
import os
import time

os.environ['DRIVER_URL'] = 'https://chromedriver.storage.googleapis.com/96.0.4664.45/chromedriver_win32.zip'
os.environ['PATH_TO_DRIVER'] = './chromedriver_win32/chromedriver.exe'

def hasDriver(path):
    return os.path.exists(path)

def set_headless_options():
    option = Options()
    option.add_argument('--headless')
    option.add_argument('--disable-gpu')
    return option

def load_driver(path):
    if not hasDriver(path):
        dload.save_unzip(os.getenv('Driver_URL'))
        path = './chromedriver_win32/chromedriver.exe'
    return webdriver.Chrome(path, chrome_options=set_headless_options())

def translate(text:str) -> str:
    set_headless_options() 
    driver = load_driver(os.getenv('PATH_TO_DRIVER'))
    driver.get("https://translate.google.com/")
    source_textarea = driver.find_element(By.CSS_SELECTOR, 'textarea[aria-label="Source text"]')
    source_textarea.send_keys(text)
    driver.implicitly_wait(3500)
    result = driver.find_element(By.CSS_SELECTOR, 'span[data-language-for-alternatives="en"] > span')
    result = result.text
    driver.close()
    return result

def correct_spell(text:str) -> str:
    pass    

if __name__ == '__main__':
    translate('ساه نڪرڻ ، دَم نڪرڻ ، مَرڻ ، وفات ڪرڻ ، پِراڻُ ڇڏڻ ، چالاڻو ڪرڻ ، لاڏاڻو ڪرڻ ، ڏيهه تِياڳڻ ، فَؤتي ٿيڻ.')