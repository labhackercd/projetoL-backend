FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1

RUN mkdir /project
WORKDIR /project

COPY requirements.txt /project

RUN pip install -r requirements.txt

COPY /project /project