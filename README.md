# recipie-app-api
Recipe app api source

install docker CE and docker compose
https://docs.docker.com/install/linux/docker-ce/ubuntu/
https://docs.docker.com/compose/install/

docker-compose run --rm app sh -c "python manage.py test && flake8"
docker-compose up
docker build .