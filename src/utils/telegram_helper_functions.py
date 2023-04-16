import requests

from utils.database_helper_functions import query_database



def update_job_delivery(conn, url):
    modify_query = f'''
            UPDATE
                jobs
            SET
                is_sent = True
            WHERE
                url = '{url}'
            '''

    query_database(conn=conn, type="update", query=modify_query)
    return


def send_job_notification(conn, job):
    company:str = job[0]
    role = job[1]
    location = job[2]
    url = job[3]
    
    message = f'{company.capitalize()}\n=====================\n\nRole - {role}\nLocation - {location}\nURL - {url}'.replace('&', '%26')
    
    url_prefix = 'https://api.telegram.org/bot5550807059:AAEFaAQ53OyWQpz23dsVWDwkKpRx-xz36T4/sendMessage'
    url_query = f'?chat_id=-776374127&text={message}'

    message_url = url_prefix + url_query
    requests.get(message_url)
    update_job_delivery(conn=conn, url=url)

    return


def get_latest_jobs(conn):
    select_query = f'''
            SELECT
                company, role, location, url
            FROM
                jobs
            WHERE
                qualify_for = True
                AND is_sent = False
            '''
    
    latest_jobs = query_database(conn=conn, type="select", query=select_query)

    return latest_jobs
