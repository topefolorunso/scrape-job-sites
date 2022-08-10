# spotify-jobs

docker build -t scrape_jobs:v01 .

docker run --name scrape_jobs -it scrape_jobs:v01

docker exec -t -i scrape_jobs bash