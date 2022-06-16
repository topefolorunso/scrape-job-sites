from scrape_functions import *

def scrape_webpage(url, path_to_file, keywords):

    job_dict = scrape_all_jobs(url)

    job_df = export_jobs_to_file(job_dict, path_to_file)
    print('export completed... 100%')

    filtered_path = 'filtered_' + path_to_file
    filter_jobs(job_df, filtered_path, *keywords)

if __name__ == '__main__':

    url = "https://www.lifeatspotify.com/jobs"
    path_to_file = 'spotify-jobs.csv'
    keywords = ('Associate', 'Engineer')

    print(f'scraping {url} ...')
    scrape_webpage(url, path_to_file, keywords)
    print('scrape job completed... 100%')