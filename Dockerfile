# pull official base image
FROM python:3.8-alpine

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

RUN apk update \
    && apk add python3-dev musl-dev mariadb-dev gcc mariadb-connector-c-dev

# install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

# add and run as non-root user
RUN adduser -D myuser
USER myuser

# run gunicorn
CMD gunicorn tuike_api.wsgi:application --bind 0.0.0.0:$PORT
