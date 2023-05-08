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


test:
	poetry run python manage.py test


makemess:
	django-admin makemessages -l ru


compilemess:
	django-admin compilemessages

shell:
	poetry run django-admin shell