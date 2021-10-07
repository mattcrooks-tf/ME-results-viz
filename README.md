# me results viz

Code to display a visualisation of ME results with significance.

## Overview

- **Project title:** me results viz
- **Inception Date:** October 2021
- **Main Stakeholder(s):** ce-ds
- **Main Stakeholder department(s):** ce-ds
- **Author(s):** Matt Crooks

#### What was the goal of the project

Code to display a visualisation of ME results with significance.

#### Outputs

What is the output of the code? This could be a report, figures, or data.

#### Documentation

Add a link to documentation - Notion page or google doc.

## Prerequisites

You'll need to install virtualenv:
```
pip install virtualenv==20.5.0
```

## Usage

1. Initialise and setup the virtualenv for the project and activate: 

    Running the command
    ```
    make create_environment
    ```
    will create the virtual environment with any required packages listed in requirements.txt.
	
    This will also install an ipykernel you can select from jupyter - The name of the kernel will be the same as your 
    repository name.

    To activate the virtual environment use
    ```
    source venv/bin/activate
    ```
 
    To add the path of the `src` folder you can run
    ```
     source .me_results_viz_env 
    ```

2. If you need to install any additional dependencies simply add them to the `requirements.txt` file and run 
   `make requirements`

    **If you are working in a jupyter notebook you will need to restart the kernel to see the changes

3. To make sure your environment is stored run `make package` before checking in (this will pick up anything you 
   installed just using pip directly)


### Run test

Unit tests will need to be stored in the `/test` folder. To run use the command

```
make test
```

Make sure to pass all tests before opening a pull request. You will also get a coverage report that shows
how much of the code in the `/src` folder is covered by the unittest - these should all be 100%.

### Linting SQL queries 

SQL queries can be stored in the `/sql` folder. These should pass the standards of ce-ds as outlined
here: https://www.notion.so/typeform/Standards-around-code-3bbee3f3684d4fe582fd6fd58b4bb0db

To check all the queries in `/sql` folder are to standard you can use sqlfluff, which has been configured
to the required standards. To run sql fluff linter use:
```
make sqlfluff_lint
```
Many violations of the rules can be fixed automatically. To this use
```
make sqlfluff_fix
```
Some rules cannot be fixed automatically so you should rerun the linter. All queries should pass the
linter before opening a pull request.
