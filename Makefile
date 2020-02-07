# Develop

check:
	black --check .
	flake8
	isort --check-only --recursive
	mypy .

checkcommit:
	black .
	flake8
	isort --recursive
	mypy .

collectstatic:
	python manage.py collectstatic --clear --noinput

dev:
	pip install -q -U pip~=20.0.1 pip-tools~=4.4.0
	pip-sync requirements/dev.txt

migrate:
	python manage.py migrate --noinput

migrations:
	python manage.py makemigrations --no-header

pip:
	pip install -q -U pip~=20.0.1 pip-tools~=4.4.0
	pip-compile $(p) requirements/common.ini > requirements/common.txt
	pip-compile $(p) requirements/dev.ini > requirements/dev.txt
	pip-compile $(p) requirements/prod.ini > requirements/prod.txt
	pip-compile $(p) requirements/tests.ini > requirements/tests.txt
	pip-compile $(p) requirements/local.ini > requirements/local.txt

test:
	tox -e coverage,reporthtml,report

# Ansible

alpha:
	cd deploy && TARGET=alpha ansible-playbook -vv deploy.yml --skip-tags "init,database,restore"

beta:
	cd deploy && TARGET=beta ansible-playbook -vv deploy.yml --skip-tags "init,database,restore"

initalpha:
	cd deploy && TARGET=alpha ansible-playbook -vv deploy.yml --skip-tags "restore"

initbeta:
	cd deploy && TARGET=beta ansible-playbook -vv deploy.yml --skip-tags "restore"

initproduction:
	cd deploy && TARGET=production ansible-playbook -vv deploy.yml --skip-tags "restore"

production:
	cd deploy && TARGET=production ansible-playbook -vv deploy.yml --skip-tags "init,database,restore"

restorealpha:
	cd deploy && TARGET=alpha ansible-playbook -vv deploy.yml --skip-tags "init"

restorebeta:
	cd deploy && TARGET=beta ansible-playbook -vv deploy.yml --skip-tags "init"

restoreproduction:
	cd deploy && TARGET=production ansible-playbook -vv deploy.yml --skip-tags "init"
