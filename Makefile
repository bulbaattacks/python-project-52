server:
	python manage.py runserver

lint:
	poetry run flake8 task_manager

PORT ?= 8000
start:
	python manage.py runserver 0.0.0.0:$(PORT)

repl:
	python manage.py shell


makemigrations:
	poetry run python manage.py makemigrations


migrate:
	poetry run python manage.py migrate

#test:
	#poetry run pytest

#test-cov:
	#poetry run pytest --cov=page_analyzer tests/ --cov-report xml