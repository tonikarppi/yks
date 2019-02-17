all: dist

install:
	python setup.py install

develop:
	python setup.py develop

dist:
	python setup.py sdist bdist_wheel

test:
	pytest
	coverage report --fail-under 70

check:
	pre-commit run --files *.py

force-publish:
	twine upload --skip-existing dist/*

publish:
	twine upload dist/*

publish-test:
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

.PHONY: install develop dist test check publish