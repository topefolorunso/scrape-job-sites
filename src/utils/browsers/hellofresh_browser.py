from browsers.browser_base_class import Browser

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

import time

def verify_human(browser):

    WebDriverWait(browser, 20).until(expected_conditions.presence_of_element_located((By.XPATH, "//input[@value='Verify you are human']")))
    verify_button = browser.find_elements(By.XPATH, "//input[@value='Verify you are human']")
    verify_button[0].click()
   
    return 


class HellofreshBrowser(Browser):

    def __init__(self, url) -> None:
        while True:
            try:
                super().__init__(url=url)
                self.num_jobs: int
                verify_human(browser=self.browser)
                break
            except TimeoutException as error:
                print('unable to verify human! retrying...')
                print('Error: ', error)
                time.sleep(3)


    def load_all_jobs(self):
        WebDriverWait(self.browser, 20).until(expected_conditions.presence_of_element_located((By.XPATH, "//span[@class='result-count']")))
        num_jobs = [int(num.text) 
            for num in self.browser.find_elements(By.XPATH, "//span[@class='result-count']")]
        self.num_jobs = num_jobs
        print('num_jobs', num_jobs, 'self.num_jobs', self.num_jobs)


    def scrape_all_jobs(self):
        return
        job_info = {}
        roles = []
        urls = []
        locations = []

        job_item = self.browser.find_elements(By.XPATH, '//div[@class="mb-xxxs mb-mobile-xxs entry_cols__3vENU entry_header__2Rw2O"]/a')
        for job in job_item:
            roles.append(job.text)
            urls.append(job.get_attribute('href'))

        job_locations = self.browser.find_elements(By.XPATH, '//div[@class="mb-xxxs mb-mobile-xxs entry_cols__3vENU entry_header__2Rw2O"]/p')
        for location in job_locations:
            locations.append(location.text)

        job_info['role'] = roles
        job_info['location'] = locations
        job_info['url'] = urls

        return (job_info)
