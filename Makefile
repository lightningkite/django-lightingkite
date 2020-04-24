help:
	@echo "clean - remove all build, test, coverage and Python artifacts"
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "clean-test - remove test and coverage artifacts"
	@echo "build - build django app for distribution"
	@echo "build-image - build docker image"
	@echo "build-docker - build django app for distribution in docker environment"
	@echo "test - run tests quickly with the default Python"
	@echo "test-docker - run tests quickly with the docker environment"
	@echo "coverage - check code coverage quickly with the default Python"
	@echo "install - install the package to the active Python's site-packages"
	@echo "docker - spin up docker environment"

clean: clean-test clean-build clean-pyc clean-

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -fr {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -fr .cache/
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/

clean-docker:
	docker rmi lightningkite/django-lightningkite

build-image:
	docker build -t lightningkite/django-lightningkite .

build:
	python setup.py sdist --formats=gztar,zip

build-docker: build-image
	docker run --rm -v $(shell pwd):/code lightningkite/django-lightningkite

shell: build-image
	docker run --rm -it -v $(shell pwd):/code lightningkite/django-lightningkite bash 

test:
	python setup.py test

test-docker: build-image
	docker run --rm -v $(shell pwd):/code lightningkite/django-lightningkite python setup.py test

coverage:
	coverage run --source django_extensions setup.py test
	coverage report -m
	coverage html

venv:
	python3 -m  venv env

install: clean
	python setup.py install
