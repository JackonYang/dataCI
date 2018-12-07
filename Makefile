PY?=python3
PIP?=pip3

build:
	$(PY) setup.py sdist bdist_wheel

upload:
	twine upload dist/*

install:
	$(PIP) install -e .


dev-setup:
	$(PIP) install -r requirements-dev.txt

test:
	pytest .

.PHONY: build upload install
.PHONY: test
.PHONY: dev-setup
