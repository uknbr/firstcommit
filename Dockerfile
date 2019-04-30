FROM python:3.7.0-alpine3.7

MAINTAINER "TechnologiesINFRABRADocker@int.amdocs.com"
LABEL group="P3WR"

ENV http_proxy "http://genproxy.amdocs.com:8080"
ENV https_proxy "http://genproxy.amdocs.com:8080"
ENV no_proxy "localhost,127.0.0.1"
ENV CUSTOM_MESSAGE="Welcome to my Docker!"

WORKDIR /app

COPY . /app
RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 1234
CMD [ "sh","startup.sh" ]
