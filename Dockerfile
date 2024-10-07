FROM python:3.12-slim

WORKDIR /app

RUN pip install pipenv

COPY Data/data.csv Data/data.csv
COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --deploy --ignore-pipfile --system

COPY customer_assist .

EXPOSE 5000

CMD gunicorn --bind 0.0.0.0:5000 app:app