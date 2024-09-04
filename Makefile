install: 
	pip install --upgrade pip && pip install -r requirements.txt

format: 
	black *.py

lint: 
	pylint *.py

test:
	python -m pytest -cov=main test_python.py
	
all: install format lint test 