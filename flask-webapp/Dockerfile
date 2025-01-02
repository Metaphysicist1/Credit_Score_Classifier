FROM python:3.11.11-slim-bullseye

RUN apt-get update
RUN apt-get install libgomp1

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile","Pipfile.lock","./"]

RUN pipenv install --deploy --system 

COPY ["*.py", "models/model.joblib", "./"]

EXPOSE 9612

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9612", "server:app"]