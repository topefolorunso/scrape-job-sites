from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time


class Browser():
    OPTIONS = Options()
    OPTIONS.add_argument('--no-sandbox')
    OPTIONS.add_argument('--window-size=1420,1080')
    OPTIONS.add_argument('--headless')
    OPTIONS.add_argument('--disable-gpu')

    DRIVER_PATH = './chromedriver.exe'
        
    def __init__(self, url) -> None:
        self.url = url
        self.browser = webdriver.Chrome(executable_path=self.DRIVER_PATH, options=self.OPTIONS)
        self.browser.get(self.url)
        time.sleep(5)
        print('webpage opened in background')
  
    def close_browser(self):
        self.browser.close()

