collectstatic:
	python manage.py collectstatic --clear --noinput

dev:
	pip install -q pip==19.1.1 pip-tools==3.9.0
	pip-sync requirements/dev.txt

pip:
	pip install -q pip==19.1.1 pip-tools==3.9.0
	pip-compile $(p) requirements/common.ini > requirements/common.txt
	pip-compile $(p) requirements/dev.ini > requirements/dev.txt
	pip-compile $(p) requirements/prod.ini > requirements/prod.txt
	pip-compile $(p) requirements/tests.ini > requirements/tests.txt
	pip-compile $(p) requirements/local.ini > requirements/local.txt

test:
	tox -e coverage,reporthtml

initalpha:
	cd deploy && TARGET=alpha ansible-playbook -vv deploy.yml

alpha:
	cd deploy && TARGET=alpha ansible-playbook -vv deploy.yml --skip-tags "init"

initbeta:
	cd deploy && TARGET=beta ansible-playbook -vv deploy.yml

beta:
	cd deploy && TARGET=beta ansible-playbook -vv deploy.yml --skip-tags "init"

initproduction:
	cd deploy && TARGET=production ansible-playbook -vv deploy.yml

production:
	cd deploy && TARGET=production ansible-playbook -vv deploy.yml --skip-tags "init"
