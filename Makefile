export SETTINGS={{project_name}}.settings.testing
export USERNAME=$(shell whoami)

# use this command in continuous integration environment (es: jenkins)
ci:
	( \
		virtualenv --python=python3.6 ${JENKINSBUILD_DIR}/{{project_name}}; \
		source ${JENKINSBUILD_DIR}/{{project_name}}/bin/activate; \
		pip install -U pip; \
		pip install -U -r requirements/tests.txt; \
		python manage.py collectstatic --clear --noinput; \
		flake8; \
		coverage run manage.py test --settings=${SETTINGS} --noinput; \
		coverage xml; \
	)

initalpha:
	( \
		cd deploy && TARGET=alpha ansible-playbook -vv deploy.yaml; \
	)

alpha:
	( \
		cd deploy && TARGET=alpha ansible-playbook -vv deploy.yaml --skip-tags "init"; \
	)

initbeta:
	( \
		cd deploy && TARGET=beta ansible-playbook -vv deploy.yaml; \
	)

beta:
	( \
		cd deploy && TARGET=beta ansible-playbook -vv deploy.yaml --skip-tags "init"; \
	)

initproduction:
	( \
		cd deploy && TARGET=production ansible-playbook -vv deploy.yaml; \
	)

production:
	( \
		cd deploy && TARGET=production ansible-playbook -vv deploy.yaml --skip-tags "init"; \
	)

test:
	( \
		coverage run manage.py test --settings=${SETTINGS} --noinput; \
		coverage html; \
	)

dev:
	( \
		pip install -q -U pip pip-tools; \
		pip-sync -q requirements/dev.txt; \
	)

# to pass optional parameters use as: make pip p='-P requests'
pip:
	( \
		pip install -q -U pip pip-tools; \
		pip-compile $(p) requirements/common.ini > requirements/common.txt; \
		pip-compile $(p) requirements/dev.ini > requirements/dev.txt; \
		pip-compile $(p) requirements/prod.ini > requirements/prod.txt; \
		pip-compile $(p) requirements/tests.ini > requirements/tests.txt; \
	)\

collectstatic:
	( \
		python manage.py collectstatic --clear --noinput; \
	)
