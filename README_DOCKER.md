# Cookiecutter Flask OpenAPI

> Docker GUIDE


### Requirements

- Install [Docker](https://docs.docker.com/engine/install/) and [docker-compose](https://docs.docker.com/compose/install/)

### Build and initialize the DB and the API containers

```
docker-compose up --build -d
```


### Create the initial database

```
docker exec flask_cookie-api  flask db upgrade
```


### Logs

```
docker logs -f flask_cookie-api
```



### Stop

```
docker-compose down
```

## Run the TEST Database

```
docker-compose -f docker-compose.test.yml up -d
```