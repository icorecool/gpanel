#!/bin/sh
#pipenv run python manage.py dumpdata --format=json plugins > plugins/fixtures/initial_data.json
#pipenv run python manage.py dumpdata --format=json php > php/fixtures/initial_data.json
pipenv run python manage.py loaddata initial_data.json