#!/bin/sh

(crontab -l && echo "0 8,12,18 * * * python ~/spotify-jobs/src/scrape_jobs.py") | crontab -

(crontab -l && echo "15 8,12,18 * * * python ~/spotify-jobs/src/run_telegram_bot.py") | crontab -