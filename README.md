# stock symbols

virtualenv .

.\Scripts\activate

deactivate

docker build -t cron .
docker run -it cron
docker run -it cron /bin/bash

docker-compose up --build


docker-compose build
docker-compose push
docker stack deploy -c docker-compose.yml symbols

docker service logs symbols_cron