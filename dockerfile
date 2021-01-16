## define python ver
FROM python:3

## i write this :v
MAINTAINER Phobos

## working directory
WORKDIR /usr/src

## copy requeiremtns.txt to workdir
COPY requirements.txt requirements.txt

## install requirements
RUN pip3 install --no-cache-dir -r requirements.txt

## copy app folder to 
COPY app app

## copy dotenv
COPY .env .env

## start main.py
ENTRYPOINT ["python3", "app/main.py"]

## expose port 8080
EXPOSE 8080