import pandas as pd
import requests
import time


def fetch_dataframe(file_name):
    df = pd.read_csv(f'../output_files/{file_name}')
    return df

def generate_messages(df):

    jobs = []
    for row in range(len(df)):
        job = ''
        for column in df:
            job += f'{column.capitalize()} - {df.loc[row, column]}\n'

        job = job.replace('&', '%26')
        jobs.append(job)

    return jobs

    # for job in jobs:
    #     print(job)


def send_message(message):

    message_url = f'https://api.telegram.org/bot5550807059:AAEFaAQ53OyWQpz23dsVWDwkKpRx-xz36T4/sendMessage?chat_id=-776374127&text={message}'
    requests.get(message_url)


if __name__ == '__main__':
    file_name = 'filtered_spotify-jobs.csv'

    message_df = fetch_dataframe(file_name)
    messages = generate_messages(message_df)

    for message in messages:
        send_message(message)
        time.sleep(5)