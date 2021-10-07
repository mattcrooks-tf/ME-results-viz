.PHONY: clean data lint requirements test
.DEFAULT_GOAL := help

#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
BUCKET = [OPTIONAL] your-bucket-for-syncing-data (do not include 's3://')
PROFILE = default
PROJECT_NAME = me-results-viz
PYTHON_INTERPRETER = python3

ifeq (,$(shell which conda))
HAS_CONDA=False
else
HAS_CONDA=True
endif

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Set up python interpreter environment and install/update dependencies
create_environment: venv/bin/activate requirements

## Install or update packages based on requirements.txt
requirements: venv/bin/activate requirements.txt
	. venv/bin/activate; \
	$(PYTHON_INTERPRETER) -m pip install -r requirements.txt; \
    $(PYTHON_INTERPRETER) -m ipykernel install --user --name=$(PROJECT_NAME)
	@echo "Requirements up to date & kernal available in notebook as $(PROJECT_NAME) - restart kernel for changes to take effect"
    @echo ">>> virtualenv created/updated. Activate with: \n(mac) source venv/bin/activate \n(Windows) venv\Scripts\activate"
	touch requirements.txt

#### Install Python Dependencies (not in virtualenv)
venv/bin/activate:
	# Create venv folder if doesn't exist. Run make clean to start over.
	test -d venv || $(PYTHON_INTERPRETER) -m venv venv
	. venv/bin/activate; \
	$(PYTHON_INTERPRETER) -m pip install -U pip setuptools wheel ipykernel
	@echo ">>> virtualenv created/updated. Activate with: \n(mac) source venv/bin/activate \n(Windows) venv\Scripts\activate"
	touch venv/bin/activate

## Make Dataset
data: requirements
	$(PYTHON_INTERPRETER) src/data/make_dataset.py

## Delete all compiled Python files and virtualenv
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
	#find . -type d -name "*.egg-info" -exec rm -rf {} \;
	rm -rf dist/
	rm -rf venv/
	rm -rf wheelhouse/

## Lint using flake8
lint:
	flake8 src

## Lint using sqlfluff
sqlfluff_lint:
	sqlfluff lint sql/*

## Lint using sqlfluff
sqlfluff_fix:
	sqlfluff fix sql/*

## Run tests
test: create_environment
	. venv/bin/activate; \
	pytest -s --cov=src/ test/ --cov-report term-missing -v

## Package dependencies to requirements.txt
package:
	pip freeze > requirements.txt

## Upload Data to S3
sync_data_to_s3:
ifeq (default,$(PROFILE))
	aws s3 sync data/ s3://$(BUCKET)/data/
else
	aws s3 sync data/ s3://$(BUCKET)/data/ --profile $(PROFILE)
endif

## Download Data from S3
sync_data_from_s3:
ifeq (default,$(PROFILE))
	aws s3 sync s3://$(BUCKET)/data/ data/
else
	aws s3 sync s3://$(BUCKET)/data/ data/ --profile $(PROFILE)
endif
