# Docker useful tips

## CLI
- `docker exec <container> <command>` - run command in running container
- `docker exec -it <container> /bin/bash` - run bash interactively
- `docker build -t <contailer_name>:<tag> <path/to/Dockerfile>` - build container
- `docker run [-d -p <host_machine_port>:<container_port> -v <path/to/host/volume>:<path/to/container/volume> --env MYVAR1=foo --env MYVAR1=bar] <container_name_or_id> [<command_to_run>]` - run options
- `docker exec -it <container_name> /bin/bash` - войти в консольк запущенного контейнера
- `docker run -it ubuntu /bin/bash` - запускает контейтер в интерактивном режиме (приглашение cmd, запускай что хочешь): `-i` оставляет STDIN открытым, `-t` назначает псевдо-tty для интерактивной связи с контейнером, `/bin/bash` - выполняемая в контейнере команда
- `docker-compose run <container> bash` - same, but with compose
- `docker port <container>` - port
- `docker ps` - list running containers
- `docker ps -a` - list all containers (and stopped too)
- `docker stop $(docker ps -a -q)` - stop all containers
- `docker rm $(docker ps -a -q)` - rm all containers
- `docker images` - list images
- `docker system prune && docker volume prune` - total cleanup (remove all containers, images, networks, volumes etc)
- `docker rmi -f $( docker images | grep localtest | awk '{print $3}' )` - удалить все образы с тэгом `localtest`
- `docker rmi -f $( docker images | grep -v localtest | awk '{print $3}' )` - удалить все образы, кроме тех, которые с тэгом `localtest`
- `docker login artifactory.setmachine.ru:5000 v.mitin <passwd>` - логинимся
- `docker inspect <container> | grep compose` - check location of docker-compose from which it was started
- `docker stat` - container's resources usage

## Dockerfile
```
FROM alpine:3.4
COPY . /app
RUN apk update && \
    apk add curl && \
    apk add git && \
    apk add vim
CMD ["sh", "-c", "/app/migrate pg up && /app/backend"]
```
## Troubleshooting:
### `could not find an available, non-overlapping IPv4 address pool among the defaults to assign to the network`
- docker network prune

##
docker-compose ps -q psql | xargs -I {} docker cp ./init_dev_data.sql {}:/tmp
docker-compose exec psql psql -U postgres -d customers -f /tmp/init_dev_data.sql

## Changing user in container from root
- https://vsupalov.com/docker-shared-permissions/
```
FROM ubuntu

ARG USER_ID
ARG GROUP_ID

RUN addgroup --gid $GROUP_ID user
RUN adduser --disabled-password --gecos '' --uid $USER_ID --gid $GROUP_ID user
USER user
```
```
$ docker build -t myimage \
  --build-arg USER_ID=$(id -u) \
  --build-arg GROUP_ID=$(id -g) .
$ docker run -it --rm \
  --mount "type=bind,src=$(pwd)/shared,dst=/opt/shared" \
  --workdir /opt/shared \
  myimage bash
```
## misc
- `ip a` - see you docker route ip (172.17.0.1), and use it instead of localhost to ping services, run on host

## remote
- `DOCKER_HOST=“ssh://user@remotehost” docker-compose up -d` - running docker in remote machine as your local
- `docker context create remote ‐‐docker “host=ssh://user@remotemachine”` - creates context
- `docker context ls`
- `docker context use remote`
- `docker context use default`
- `docker --context remote ps`
- `docker-compose --context=remote up`

