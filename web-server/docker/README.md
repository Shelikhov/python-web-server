# Dockerfile
A  Dockerfile for building a Python application on docker.

## Description 
A Python application that support services:
  It responds to the URL like 'http://host/?n=x' where x is a number and returns n*n;
  It responds to the URL like 'http://host/blacklisted' with conditions:
    - to return error code 444 to the visitor
    - block the IP address of the visitor, the following attempts to gain access with this IP will return a 403 error
    - send an email with visitor's IP to an email (params in values.yaml app.emailNotification)
    - to insert into PostgreSQL table (table name blacklisted, scheme name web_server, database web_server, user web_server) information like:
      - URL path (in this case /blacklisted)
      - visitor's IP address
      - date and time when the visitor got blocked

### Building example
  $ docker build path-to-the-dockerfile -t name-of-your-image

### Description of source files
server.py - HTTP server
mail.py - to send notification (client IP) to the special email
psql.py - to connect, read, write data from PostgreSQL database
