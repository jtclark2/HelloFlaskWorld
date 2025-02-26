install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black *.py
	
lint:
	pylint --disable=R,C main.py test_hello.py
	
test:
	python -m pytest -vv --cov=main test_hello.py
	
all: install format lint test
