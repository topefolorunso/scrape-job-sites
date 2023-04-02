from helper_functions import *

companies = ('spotify', 'zalando',)

keywords_dict = {
    'spotify': ('Associate', 'Engineer'), 
    'zalando': ('Engineer'), 
    'hellofresh': ('Junior', 'Engineer'),
    }

urls_dict = {
    'spotify': "https://www.lifeatspotify.com/jobs", 
    'zalando': "https://jobs.zalando.com/en/jobs",
    'hellofresh': "https://careers.hellofresh.com/global/en/search-results"
    }

def scrape_webpage(company, url, file_name, keywords):
    job_dict = scrape_all_jobs(company, url)

    path_to_file = get_file_path(file_name)
    job_df = export_jobs_to_file(job_dict, path_to_file)
    print('export completed... 100%')

    filtered_path = get_file_path('filtered_' + file_name)
    filter_jobs(job_df, filtered_path, *keywords, type=company)

if __name__ == '__main__':

    connect_to_database()

    for company in companies:
        keywords = keywords_dict[company]
        url = urls_dict[company]
        file_name = f'{company}-jobs.csv'

        print(f'scraping {company} job site ...')
        scrape_webpage(company, url, file_name, keywords)

    print('scrape job completed... 100%')