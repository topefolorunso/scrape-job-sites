from scrape_functions import *

def scrape_webpage(url, file_name, keywords):

    job_dict = scrape_all_jobs(url)

    path_to_file = get_file_path(file_name)
    job_df = export_jobs_to_file(job_dict, path_to_file)
    print('export completed... 100%')

    filtered_path = get_file_path('filtered_' + file_name)
    filter_jobs(job_df, filtered_path, *keywords)

if __name__ == '__main__':

    url = "https://www.lifeatspotify.com/jobs"
    file_name = 'spotify-jobs.csv'
    keywords = ('Associate', 'Engineer')

    print(f'scraping {url} ...')
    scrape_webpage(url, file_name, keywords)
    print('scrape job completed... 100%')