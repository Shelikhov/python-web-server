FROM docker.io/postgres:12
COPY ./web-server-db.sql /docker-entrypoint-initdb.d/web-server-db.sql
EXPOSE 5432