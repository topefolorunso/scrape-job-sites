#!/bin/sh

(echo "0 8,12,18 * * * python /src/scrape_jobs.py" && echo "15 8,12,18 * * * python /src/run_telegram_bot.py") | crontab -