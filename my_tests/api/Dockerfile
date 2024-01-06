FROM python:3.9.10-alpine

WORKDIR /tests_project

COPY requirements.txt .

RUN pip install -r requirements.txt && mkdir logs
ENV ENV=env

CMD python -m pytest -s --alluredir=test_results/ /tests_project/tests