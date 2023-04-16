from utils.browsers.spotify_browser import SpotifyBrowser
from utils.browsers.zalando_browser import ZalandoBrowser
from utils.browsers.hellofresh_browser import HellofreshBrowser
from utils.database_helper_functions import query_database



def update_qualified_jobs(conn, keywords, company):

    keyword_clause = ' AND '.join([f"role LIKE '%{keyword}%'" for keyword in keywords])
    main_query = f'''
            UPDATE
                jobs
            SET
                qualify_for = True
            WHERE
                {keyword_clause}
                AND company = '{company}'
            '''
    
    if company=='zalando':
        exp_keywords = ('Apprenticeship', 'Graduate', 'Entry', 'Intern', 'Trainee')
        exp_keyword_clause = ' OR '.join([f"experience_level LIKE '%{exp_keyword}%'" for exp_keyword in exp_keywords])

        modify_query =  f'''
            {main_query}
                AND ({exp_keyword_clause})
            '''
        
        # print (modify_query)
        query_database(conn=conn, type="update", query=modify_query)

    else:
        modify_query =  main_query
        # print (modify_query)
        query_database(conn=conn, type="update", query=modify_query)

    return


def insert_jobs_to_db(job_dict, conn):

    columns = ", ".join(job_dict.keys())
    values = [
        f'''({', '.join(
            (f'"{str(job_dict[key][i])}"' 
                for key in job_dict.keys())
            )})'''

            for i in range(len(list(job_dict.values())[0]))
        ]

    insert_query = f'''
        INSERT OR IGNORE INTO 
            jobs ({columns})
        VALUES
            {', '.join(values)}
        '''
    
    # job_df = pd.DataFrame(job_dict)
    print(f'inserting jobs to database ...')
    query_database(conn=conn, type="insert", query=insert_query)
    # job_df.to_sql('jobs', con=db_engine, if_exists='append', index=False)
    print('insertion completed... 100%')

    return


def scrape_all_jobs(company: str, url) -> dict:

    browser_class_name = company.capitalize() + 'Browser'
    browser = eval(browser_class_name)(url)

    browser.load_all_jobs()
    job_info = browser.scrape_all_jobs()
    browser.close_browser()

    return job_info


def scrape_webpage(company, url, conn, keywords):

    job_dict = scrape_all_jobs(company, url)
    insert_jobs_to_db(job_dict=job_dict, conn=conn)
    update_qualified_jobs(conn=conn, keywords=keywords, company=company)
    
    return