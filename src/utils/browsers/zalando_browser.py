import time

from selenium.webdriver.common.by import By

from utils.browsers.browser_base_class import Browser



class ZalandoBrowser(Browser):

    def __init__(self, url) -> None:
        super().__init__(url=url)
        self.max_page = 1
        

    def load_all_jobs(self):
        max_page = max(set(
            int(num.text) 
            for num in self.browser.find_elements(By.XPATH, "//li[@class='pagination__button']")
            ))
        self.max_page = max_page

    def scrape_all_jobs(self):
        
        job_info = {}
        roles = []
        urls = []
        locations = []
        exps = []

        curr_page = 1
        while curr_page <= self.max_page:
            job_titles = self.browser.find_elements(By.XPATH, "//div[@class='card--job-result__title-container']/span[@class='card--job-result__title']")
            for job in job_titles:
                roles.append(job.text)

            job_locations = self.browser.find_elements(By.XPATH, '//div[@class="card--job-result__locations-container"]')
            for location in job_locations:
                locations.append(location.text)

            links = [link_item.get_attribute('href') for link_item in self.browser.find_elements(By.XPATH, "//li[@class='card-outer']/a")]
            for link in links:
                urls.append(link)
                
                while True:
                    try:
                        self.browser.get(link)
                        time.sleep(2)

                        experience_level = [elem.text.split('\n')[1] for elem in self.browser.find_elements(By.XPATH, '//div[h2[contains(text(),"Experience Level")]]')]
                        exps.extend(experience_level)
                        
                        break
                    except IndexError:
                        continue

            if curr_page==self.max_page:
                break

            curr_page+=1
            next_page = f"https://jobs.zalando.com/en/jobs?page={curr_page}"
            self.browser.get(next_page)
            time.sleep(5)

        job_info['role'] = roles
        job_info['exp_level'] = exps
        job_info['location'] = locations
        job_info['url'] = urls
        job_info['company'] = ['zalando'] * len(urls)

        return job_info


