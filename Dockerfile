FROM python:3.7.0-alpine3.7

MAINTAINER "Pedro Pavan"
LABEL version="1"

ENV CUSTOM_MESSAGE="Welcome to my Docker!"

WORKDIR /app

COPY . /app
RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 1234
CMD [ "sh","startup.sh" ]
