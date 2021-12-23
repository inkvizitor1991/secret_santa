# Makefile (use for automation routime things)
# for use type $make <commands from list below>
# example $make run
# autocomplete work as well!

## Prepare and run section (install depend-s and run server)
run: prepare
	poetry run python manage.py runserver
prepare:
	python -m pip install --upgrade pip poetry

## Django section
shell:
	poetry shell
django_shell:
	poetry run python manage.py shell
migrations:
	poetry run python manage.py makemigrations
migrate:
	poetry run python manage.py migrate
check:
	poetry run python manage.py check
superuser:
	poetry run python manage.py createsuperuser
