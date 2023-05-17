### Hexlet tests and linter status:
[![Actions Status](https://github.com/bulbaattacks/python-project-52/workflows/hexlet-check/badge.svg)](https://github.com/bulbaattacks/python-project-52/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/a8cdbf42b015d0b4e84e/maintainability)](https://codeclimate.com/github/bulbaattacks/python-project-52/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/a8cdbf42b015d0b4e84e/test_coverage)](https://codeclimate.com/github/bulbaattacks/python-project-52/test_coverage)

### About
Task Manager system allows you to create tasks, assign executors and update their statuses.
You can take a look at deployed app [here](https://python-project-52-production-409d.up.railway.app)

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