# python part
.PHONY: help test run

VENV_NAME?=.env
VENV_ACTIVATE=. $(VENV_NAME)/bin/activate
PYTHON=${VENV_NAME}/bin/python3

.DEFAULT: help

help:
	@echo "make test"
	@echo "       run tests"
	@echo "make run"
	@echo "       run project"


test:
	${PYTHON} -m pytest

run:
	${PYTHON} app.py

# Docker part
docker__build:
	docker build -t ${USER}/pokedex_py .

docker__up:
	docker run --name pokedex_py -p 5000:5000 ${USER}/pokedex_py

docker__stop:
	docker stop pokedex_py

docker__rm:
	docker rm pokedex_py

docker__down:  docker__stop docker__rm

docker__image-rm:
	docker image rm ${USER}/pokedex_py
