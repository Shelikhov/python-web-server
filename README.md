## Description 
A Python application (web-server) with database based on PostgreSQL (postgresql) that supports services:
  It responds to the URL like 'http://host/?n=x' where x is a number and returns n*n;
  It responds to the URL like 'http://host/blacklisted' with conditions:
    - to return error code 444 to the visitor
    - block the IP address of the visitor, the following attempts to gain access with this IP will return a 403 error
    - send an email with visitor's IP to an email (params in values.yaml app.emailNotification)
    - to insert into PostgreSQL table (table name blacklisted, scheme name web_server, database web_server, user web_server) information like:
      - URL path (in this case /blacklisted)
      - visitor's IP address
      - date and time when the visitor got blocked

