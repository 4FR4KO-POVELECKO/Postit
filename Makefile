.DEFAULT_GOAL := run

.PHONY: run
.PHONY: makemigrations
.PHONY: migrate


run:
	python3 ./src/manage.py runserver 0.0.0.0:8080

migrations:
	python3 ./src/manage.py makemigrations

migrate:
	python3 ./src/manage.py migrate
