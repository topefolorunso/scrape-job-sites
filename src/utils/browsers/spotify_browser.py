import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait

from browser_base_class import Browser



class SpotifyBrowser(Browser):

    def __init__(self, url) -> None:
        super().__init__(url=url)
        

    def load_all_jobs(self):
        WebDriverWait(self.browser, 20).until(expected_conditions.presence_of_element_located((By.XPATH, '//button')))
        all_buttons = {
            button.text:button 
            for button in self.browser.find_elements(By.XPATH, '//button')
            }

        print('loading all jobs...')
        while True:
            try:
                load_more_button = all_buttons['Load more jobs']

                self.browser.execute_script("arguments[0].scrollIntoView(true);", load_more_button)
                load_more_button.click()

                WebDriverWait(self.browser, 20).until(expected_conditions.presence_of_element_located((By.XPATH, '//button')))
                all_buttons = {
                    button.text:button 
                    for button in self.browser.find_elements(By.XPATH, '//button')
                    }
                
            except KeyError:
                print('all jobs loaded...')
                break
            except WebDriverException as error:
                print('page crashed')
                print('Error: ', error)
                time.sleep(3)


    def scrape_all_jobs(self):
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
        job_info['company'] = ['spotify'] * len(urls)

        return (job_info)
