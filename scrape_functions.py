from doctest import FAIL_FAST
from textwrap import indent
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

import time


class Browser():
    def __init__(self, url) -> None:
        self.url = url
        options = Options()
        options.headless = True

        self.browser = webdriver.Firefox(options=options)
        self.browser.get(self.url)

        time.sleep(5)
        print('webpage opened in background')
        

    def load_all_jobs(self):
        all_buttons = self.browser.find_elements(By.XPATH, '//button')
        # for text in [button.text for button in all_buttons]:
        #     print(text)
        # n = 1

        print('loading all jobs...')
        while 'Load more jobs' in [button.text for button in all_buttons]:
            # print(n)
            # n+=1
            for button in all_buttons:
                if button.text == 'Load more jobs':
                    button.click()
            all_buttons = self.browser.find_elements(By.XPATH, '//button')
        print('all jobs loaded...')

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

        return(job_info)

     
class DataFrame():

    def __init__(self, dict=None) -> None:
        if not dict:
            self.df = pd.DataFrame(dict)
        else:
            self.df = pd.DataFrame()

    def add_column_to_dataframe(self, column, values):

        self.df[column] = values

    def export_to_file(self, path_to_file):
        print(f'exporting data to {path_to_file} ...')
        self.df.to_csv(path_to_file)

        

def scrape_all_jobs(url):
    browser = Browser(url)
    
    browser.load_all_jobs()
    job_info = browser.scrape_all_jobs()
    return job_info

def export_jobs_to_file(job_dict, path_to_file):
    job_df = pd.DataFrame(job_dict)

    print(f'exporting data to {path_to_file} ...')
    job_df.to_csv(path_to_file, index=False)
    return job_df

def filter_jobs(df, path_to_file, *args):
    filtered_df = df

    for keyword in args:
        filtered_df = filtered_df[filtered_df.role.str.contains(keyword)]

    filtered_df.to_csv(path_to_file, index=False)
    return filtered_df