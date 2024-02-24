# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.10-slim

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# RUN apt-get update \
#     && apt-get upgrade -y \
#     && 
RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

# store all application in dedicated folder
COPY . /app
WORKDIR /app

EXPOSE 8080

# externalized launching commands
COPY ./entrypoint.sh .
ENTRYPOINT [ "sh", "/app/entrypoint.sh" ]
# CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8080

# to associate built images to the GH repo
LABEL org.opencontainers.image.source="https://github.com/CorentinBaudet/hello-devops-api"