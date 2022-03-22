CREATE USER web_server PASSWORD 'temporary_pswd' NOCREATEDB NOCREATEROLE NOSUPERUSER;
CREATE DATABASE web_server OWNER web_server ENCODING 'UTF8' LC_COLLATE='en_US.utf8' LC_CTYPE='en_US.utf8' CONNECTION LIMIT = 20;
\c web_server
CREATE SCHEMA web_server_sch AUTHORIZATION web_server;
ALTER DATABASE web_server SET search_path TO web_server_sch;
\c web_server
CREATE TABLE blacklisted (url_path VARCHAR(30) NOT NULL, client_ip VARCHAR(10) UNIQUE NOT NULL, date_time VARCHAR(30) NOT NULL);
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA web_server_sch TO web_server;