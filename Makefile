test:
	python -m pytest -vv test.py

dependencies:
	python -m pip install -r requirements.txt

all: dependencies test