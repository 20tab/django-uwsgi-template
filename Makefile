
initalpha:
	( \
		cd deploy && TARGET=alpha ansible-playbook -vv deploy.yml; \
	)

alpha:
	( \
		cd deploy && TARGET=alpha ansible-playbook -vv deploy.yml --skip-tags "init"; \
	)

initbeta:
	( \
		cd deploy && TARGET=beta ansible-playbook -vv deploy.yml; \
	)

beta:
	( \
		cd deploy && TARGET=beta ansible-playbook -vv deploy.yml --skip-tags "init"; \
	)

initproduction:
	( \
		cd deploy && TARGET=production ansible-playbook -vv deploy.yml; \
	)

production:
	( \
		cd deploy && TARGET=production ansible-playbook -vv deploy.yml --skip-tags "init"; \
	)

test:
	( \
		coverage run manage.py test --settings={{project_name}}.settings --configuration=Testing --noinput; \
		coverage html; \
	)

dev:
	( \
		pip install -q -U pip pip-tools; \
		pip-sync -q requirements/dev.txt; \
	)

pip:
	( \
		pip install -q -U pip pip-tools; \
		pip-compile $(p) requirements/common.ini > requirements/common.txt; \
		pip-compile $(p) requirements/dev.ini > requirements/dev.txt; \
		pip-compile $(p) requirements/prod.ini > requirements/prod.txt; \
		pip-compile $(p) requirements/tests.ini > requirements/tests.txt; \
		pip-compile $(p) requirements/local.ini > requirements/local.txt; \
	)\

collectstatic:
	( \
		python manage.py collectstatic --clear --noinput; \
	)
