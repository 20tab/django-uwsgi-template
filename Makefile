check:
	black --check .
	flake8
	isort --check-only --recursive
	mypy .

checkcommit:
	pre-commit run --all-files

collectstatic:
	python manage.py collectstatic --clear --noinput

migrate:
	python manage.py migrate --noinput

dev:
	pip install -q pip==19.2.3 pip-tools==4.1.0
	pip-sync requirements/dev.txt

pip:
	pip install -q pip==19.2.3 pip-tools==4.1.0
	pip-compile $(p) requirements/common.ini > requirements/common.txt
	pip-compile $(p) requirements/dev.ini > requirements/dev.txt
	pip-compile $(p) requirements/prod.ini > requirements/prod.txt
	pip-compile $(p) requirements/tests.ini > requirements/tests.txt
	pip-compile $(p) requirements/local.ini > requirements/local.txt

test:
	tox -e coverage,reporthtml,report

initalpha:
	cd deploy && TARGET=alpha ansible-playbook -vv deploy.yml --skip-tags "restore"

alpha:
	cd deploy && TARGET=alpha ansible-playbook -vv deploy.yml --skip-tags "init,database,restore"

restorealpha:
	cd deploy && TARGET=alpha ansible-playbook -vv deploy.yml --skip-tags "init"

initbeta:
	cd deploy && TARGET=beta ansible-playbook -vv deploy.yml --skip-tags "restore"

beta:
	cd deploy && TARGET=beta ansible-playbook -vv deploy.yml --skip-tags "init,database,restore"

restorebeta:
	cd deploy && TARGET=beta ansible-playbook -vv deploy.yml --skip-tags "init"

initproduction:
	cd deploy && TARGET=production ansible-playbook -vv deploy.yml --skip-tags "restore"

production:
	cd deploy && TARGET=production ansible-playbook -vv deploy.yml --skip-tags "init,database,restore"

restoreproduction:
	cd deploy && TARGET=production ansible-playbook -vv deploy.yml --skip-tags "init"
