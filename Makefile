PYTHON ?= python3
PYB ?= pyb
.DEFAULT_GOAL := all
.PHONY: all clean install install_deps test lint build package

install: install_deps
install_deps:
	$(PYTHON) -m pip install -r requirements.txt

test:
	$(PYB) run_unit_tests

lint:
	$(PYTHON) -m flake8 src tests build.py

build:
	$(PYB) publish

package: build

clean:
	$(PYB) clean

all:
	$(MAKE) clean
	$(MAKE) install_deps
	$(MAKE) test
	$(MAKE) lint
	$(MAKE) build
