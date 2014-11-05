CURRENT_VERSION=$(shell python3 -c "from flask_gladiator import get_version; print(get_version())")
NEXT_VERSION=$(shell python3 -c "from flask_gladiator import next_version; print(next_version())")


build:
	python3 setup.py sdist

test:
	tox


clean:
	rm -rf Flask-Gladiator.egg-info
	rm -f dist/*.tar.gz

inc_version:
	perl -i -pe 's/$(CURRENT_VERSION)/$(NEXT_VERSION)/' flask_gladiator/__init__.py
	echo "New vesion is: $(NEXT_VERSION)"

git_tag:
	git tag $(CURRENT_VERSION)

pypi_upload:
	python3 setup.py sdist upload -r pypi

pypi_register:
	python3 setup.py register -r pypi

pypitest_upload:
	python3 setup.py sdist upload -r pypitest

pypitest_register:
	python3 setup.py register -r pypitest
