import time

from utils.database_helper_functions import connect_to_database
from utils.telegram_helper_functions import get_latest_jobs, send_job_notification



if __name__ == '__main__':

    conn = connect_to_database()

    try:
        latest_jobs = get_latest_jobs(conn)
        
        for job in latest_jobs:
            send_job_notification(conn=conn, job=job)
            time.sleep(5)

    except Exception as e:
        raise e

    finally:
        conn.close()
        print('Database connection closed')