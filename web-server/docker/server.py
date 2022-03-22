from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
from psql import db_connect, db_insert, check_ip
from mail import send_email
import urllib.parse
import os
from time import time, ctime

server_name = os.getenv('SERVER_NAME')
server_port = int(os.getenv('SERVER_PORT'))
ip_blocked = False
db_conn = None
db_host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')
db_user = os.getenv('DB_USER')
db_pass = os.getenv('DB_PASSWORD')
gmail_sender = os.getenv('GMAIL_SENDER')
gmail_sender_pass = os.getenv('GMAIL_PASSWORD')
gmail_receiver = os.getenv('GMAIL_RECEIVER')
gmail_notification = os.getenv('GMAIL_NOTIFICATION')
gmail_smtp_addr = os.getenv('GMAIL_SMTP_ADDRESS')

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        ip_blocked = check_ip(db_conn, self.client_address[0])
        if ip_blocked:
            self.send_error(403, 'HTTP_ERROR 403')
        elif self.path == "/blacklisted":
            self.send_error(444, 'HTTP_ERROR 444')
            client_ip = str(self.client_address[0])
            date_time = ctime()
            db_insert(db_conn, self.path, client_ip, date_time)
            if gmail_notification:
                send_email(self.client_address[0], gmail_sender, gmail_sender_pass, gmail_receiver, gmail_smtp_addr)
        elif urlparse(self.path).query != '':
            query = urlparse(self.path).query
            result = pow(int(urllib.parse.parse_qs(query)['n'][0]), 2)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(bytes(str(result), "utf-8"))
        elif self.path == "/health/readiness":
            content = "Server UP"
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            self.wfile.write(content.encode("utf-8"))
        elif self.path == "/health/liveness":
            content = "Server UP"
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            self.wfile.write(content.encode("utf-8"))
        else:
            content = "not found"
            self.send_response(404)
            self.send_header("Content-Type", "text/html")
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            self.wfile.write(content.encode("utf-8"))

if __name__ == "__main__":        
    db_conn = db_connect(db_host, db_name, db_user, db_pass)
    webServer = HTTPServer((server_name, server_port), MyServer)
    print("Server started http://%s:%s" % (server_name, server_port))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    if db_conn is not None:
        db_conn.close()
        print('Database connection closed.')

    webServer.server_close()
    print("Server stopped.")
