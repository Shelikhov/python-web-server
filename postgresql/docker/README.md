# Dockerfile
A Dockerfile for building a PostgreSQL database on docker.

## Description 
Database based on PostgreSQL that contains from:
  - web_server database;
  - web_server scheme;
  - blacklisted table;
  - web_server user.

### Building example
  $ docker build path-to-the-dockerfile -t name-of-your-image
  $ docker run --name name-of-your-container -d image-id

