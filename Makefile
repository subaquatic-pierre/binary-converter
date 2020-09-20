test:
	python -m pytest -vv test.py

dependencies:
	python -m pip install -r requirement.txt

all: dependencies test