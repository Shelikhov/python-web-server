FROM python:3.8-slim-buster
WORKDIR /app
COPY ./*.py ./
RUN apt-get update
RUN apt-get install python-psycopg2 -y
RUN pip install psycopg2-binary
ENTRYPOINT python3 server.py
EXPOSE 8080