from scrape_functions import *

def scrape_webpage(url, path_to_file):

    job_dict = scrape_all_jobs(url)

    export_jobs_to_file(job_dict, path_to_file)
    print('export completed... 100%')

if __name__ == '__main__':

    url = "https://www.lifeatspotify.com/jobs"
    path_to_file = 'spotify-jobs.csv'

    print(f'scraping {url} ...')
    scrape_webpage(url, path_to_file)
    print('scrape job completed... 100%')