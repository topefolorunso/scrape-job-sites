import pandas as pd
import requests
import time


companies = ['spotify', 'zalando']

def fetch_dataframe(file_name):
    file_path = f'output_files/{file_name}'

    while True:
        try:
            df = pd.read_csv(file_path, usecols=['role', 'location', 'url'])
            break

        except FileNotFoundError:
            job_header = ['role', 'location', 'url']
            pd.DataFrame(columns=job_header).to_csv(file_path, index=False)
            continue

    return df

def update_cache(cache_file, roles, locations, urls):
    new_job_info = {}

    new_job_info['role'] = roles
    new_job_info['location'] = locations
    new_job_info['url'] = urls

    new_df = pd.DataFrame(new_job_info)
    new_df.to_csv(f'output_files/{cache_file}', index=False, mode='a', header=False)
    return

def generate_messages(df, cache_df, cache_file):

    cache_indx = cache_df.set_index(['role', 'location']).index

    latest_jobs = []

    new_roles = []
    new_urls = []
    new_locations = []

    for row in range(len(df)):
        role = df.loc[row, 'role']
        location = df.loc[row, 'location']

        if (role, location) not in cache_indx:
            url = df.loc[row, 'url']
            job = f'Role - {role}\nLocation - {location}\nURL - {url}'
            job = job.replace('&', '%26')

            latest_jobs.append(job)

            new_roles.append(role)
            new_locations.append(location)
            new_urls.append(url)

    if len(new_roles)!=0 and len(new_locations)!=0 and len(new_urls)!=0:
        update_cache(cache_file=cache_file, roles=new_roles, locations=new_locations, urls=new_urls)

    return latest_jobs


def send_message(message):
    # print(message)

    url_prefix = 'https://api.telegram.org/bot5550807059:AAEFaAQ53OyWQpz23dsVWDwkKpRx-xz36T4/sendMessage'
    url_query = f'?chat_id=-776374127&text={message}'

    message_url = url_prefix + url_query
    requests.get(message_url)


if __name__ == '__main__':

    for company in companies:
        found_jobs = f'filtered_{company}-jobs.csv'
        cached_jobs = f'cached_{company}-jobs.csv'

        new_jobs_df = fetch_dataframe(found_jobs)
        cached_df = fetch_dataframe(cached_jobs)

        latest_jobs = generate_messages(new_jobs_df, cached_df, cached_jobs)

        for job in latest_jobs:
            send_message(message=job)
            time.sleep(5)