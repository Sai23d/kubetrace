SHELL := /bin/bash

up:
	docker compose up --build -d

down:
	docker compose down

logs:
	docker compose logs -f --tail=200

test:
	python -m pytest -q

k6:
	k6 run k6/basic.js
