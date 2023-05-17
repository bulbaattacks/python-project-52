server:
	python manage.py runserver

lint:
	poetry run flake8 task_manager

PORT ?= 8000
start:
	python manage.py runserver 0.0.0.0:$(PORT)

repl:
	python manage.py shell


make-migrations:
	poetry run python manage.py makemigrations


migrate:
	poetry run python manage.py migrate


test:
	poetry run python manage.py test


make-messages:
	django-admin makemessages -l ru


compile-messages:
	django-admin compilemessages

shell:
	poetry run django-admin shell