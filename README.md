# symbols service

#### initialize virtual environment
```
virtualenv .
cd Scripts
activate
deactivate
```

#### run without docker
```
python cron.py
```

#### basic docker commands
```
docker build -t cron .
docker run -it cron
docker run -it cron /bin/bash
```

#### run with docker-compose
```
docker-compose up -d service_name
docker-compose up --build
```

#### start a docker service (docker swarm)
```
docker-compose build --no-cache
docker-compose push
docker stack deploy -c docker-compose.yml symbols

docker service ls
docker service logs symbols_cron --follow
```