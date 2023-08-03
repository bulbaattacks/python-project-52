### Hexlet tests and linter status:
[![Actions Status](https://github.com/bulbaattacks/python-project-52/workflows/hexlet-check/badge.svg)](https://github.com/bulbaattacks/python-project-52/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/a8cdbf42b015d0b4e84e/maintainability)](https://codeclimate.com/github/bulbaattacks/python-project-52/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/a8cdbf42b015d0b4e84e/test_coverage)](https://codeclimate.com/github/bulbaattacks/python-project-52/test_coverage)

### About

CRUD приложение «Менеджер задач» – это система управления задачами, подобная http://www.redmine.org/. Она позволяет создавать задачи, назначать исполнителей и менять их статусы, удалять различные сущности. Для работы с системой требуется регистрация и аутентификация пользователя. Проект выполнен на фреймворке Django, использована технология ORM, код покрыт тестами с помощью фреймворка pytest.

The CRUD Task Manager application is a task management system like http://www.redmine.org/. It allows you to create tasks, assign executors and change their statuses, delete various entities. User registration and authentication is required to work with the system.
The project is made on the Django framework, ORM technology is used, the code is covered with tests using the pytest framework.

### How to run

- Clone this repository 
- Install dependencies by poetry install 
- Copy the content from .env.sample and paste it in your .env file. cp .env.sample .env 
- Run a command 
```
make server
```

### Build with:

- python 3.9
- django
- django-bootstrap4
- requests
- pytest
- flake8
