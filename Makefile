test:
	python -m pytest -vv test.py

dependencies:
	python -m pip install -r requirements.txt

lint:
	pylint --disable=R,C,E1120,W0613 convert.py

all: dependencies test