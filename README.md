# stock symbols

virtualenv .

.\Scripts\activate

deactivate

docker build -t cron .
docker run -it cron
docker run -it cron /bin/bash