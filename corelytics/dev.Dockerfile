FROM python:3.8-slim

WORKDIR /opt/corelytics
COPY  . .
RUN pip install -r requirements.txt
