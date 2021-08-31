# Note that you should be in your virtual environment of choice before running make

MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules
MAKEFLAGS += --no-builtin-variables

WGET = /usr/bin/env wget --timestamping --no-verbose

.DEFAULT_GOAL := all
SHELL := bash

.PHONY: all
all: \
	install-flit \
	install-koza \
	install-dev \
	biolink-model.yaml \
	biolink_model_pydantic/model.py \
	format \
	test

.PHONY: FORCE
FORCE:

.PHONY: install-flit
install-flit:
	pip install flit

.PHONY: install-koza
install-koza: install-flit
	flit install --deps production --symlink

.PHONY: install-dev
install-dev: install-flit
	flit install --deps develop --symlink

.PHONY: test
test: install-flit install-dev biolink_model_pydantic/model.py
	python -m pytest

.PHONY: build
build:
	flit build

.PHONY: publish
publish: format
	flit publish

.PHONY: clean
clean:
	rm -rf `find . -name __pycache__`
	rm -f `find . -type f -name '*.py[co]' `
	rm -rf .pytest_cache
	rm -rf dist

.PHONY: lint
lint:
	flake8 --exit-zero --max-line-length 120 biolink/ tests/ pydanticgen/
	black --check --diff biolink_model_pydantic tests pydanticgen
	isort --check-only --diff biolink_model_pydantic tests pydanticgen

.PHONY: format
format:
	autoflake \
		--recursive \
		--remove-all-unused-imports \
		--remove-unused-variables \
		--ignore-init-module-imports \
		--in-place biolink_model_pydantic tests pydanticgen
	isort biolink_model_pydantic tests pydanticgen
	black biolink_model_pydantic tests pydanticgen

biolink-model.yaml: FORCE
	$(WGET) https://raw.githubusercontent.com/biolink/biolink-model/master/biolink-model.yaml

biolink_model_pydantic/model.py: install-dev biolink-model.yaml
	pydanticgen/pydanticgen.py biolink-model.yaml > biolink_model_pydantic/model.py
