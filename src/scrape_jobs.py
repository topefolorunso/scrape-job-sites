import chromedriver_autoinstaller

from utils.scraper_helper_functions import scrape_webpage
from utils.database_helper_functions import connect_to_database
from config import *


if __name__ == '__main__':

    chromedriver_autoinstaller.install()

    conn = connect_to_database()
    
    try:
        for company in COMPANIES:
            keywords = KEYWORDS_MAP[company]
            url = URLS_MAP[company]
            file_name = f'{company}-jobs.csv'

            print(f'scraping {company} job site ...')
            scrape_webpage(company, url, conn, keywords)
            print('scrape job completed... 100%')

    except Exception as e:
        print(e)

    finally:
        conn.close()
        print('Database connection closed')