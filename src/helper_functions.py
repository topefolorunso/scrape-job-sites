import os
import pandas as pd

import sqlite3

from browsers.spotify_browser import SpotifyBrowser
from browsers.zalando_browser import ZalandoBrowser
from browsers.hellofresh_browser import HellofreshBrowser


def scrape_all_jobs(company: str, url):
    browser_class_name = company.capitalize() + 'Browser'
    browser = eval(browser_class_name)(url)

    browser.load_all_jobs()
    job_info = browser.scrape_all_jobs()

    browser.close_browser()
    return job_info

def connect_to_database():
    try:
        conn = sqlite3.connect('../database/jobs.db')
        print('Database connection iniialized')
    except sqlite3.Error as error:
        print('Error occurred: ', error)
    return conn

def query_database(conn, query):
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
    except sqlite3.Error as error:
        print('Error occurred: ', error)
    finally:
        if conn:
            conn.close()
            print('Database connection closed')
        return result

def export_jobs_to_file(job_dict, path_to_file):
    job_df = pd.DataFrame(job_dict)

    print(f'exporting data to {path_to_file} ...')
    job_df.to_csv(path_to_file, index=False)
    return job_df


def filter_jobs(df, path_to_file, *args, type):
    filtered_df = df

    if type=='zalando':
        keywords = 'Apprenticeship|Graduate|Entry|Intern|Trainee'
        filtered_df = filtered_df[filtered_df.exp_level.str.contains(keywords)]
    for keyword in args:
        filtered_df = filtered_df[filtered_df.role.str.contains(keyword)]

    filtered_df.to_csv(path_to_file, index=False)
    return


def get_file_path(file_name):
    dir = 'output_files/'
    if not os.path.exists(dir):
        os.mkdir(dir)

    path_to_file = os.path.join(dir, file_name)
    return path_to_file