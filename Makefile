all: dist

install:
	python setup.py install

develop:
	python setup.py develop

dist:
	python setup.py sdist bdist_wheel

test:
	python setup.py test
	coverage report --fail-under 70

.PHONY: install develop dist test