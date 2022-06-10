.PHONY: test project

pylint:
	pylint --reports=y ./project

pytest:
	pytest

# Total pytest coverage report
coverage:
	pytest --cov=./project --cov-report xml:cov.xml
	coverage report -m

# Auto format the python file to increase pylint score
black:
	black ./project

# Gives a UML diagram for project folder
uml:
	pyreverse -o png ./project
