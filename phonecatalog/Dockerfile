FROM python:3.10

RUN mkdir -p /opt/backend
WORKDIR /opt/backend

COPY requirements.txt /opt/backend
RUN pip install -r requirements.txt

EXPOSE 8000
