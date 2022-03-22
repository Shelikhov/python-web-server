import psycopg2

def db_connect(db_host, db_name, db_user, db_pass):
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        db_conn = psycopg2.connect(host=db_host, database=db_name, user=db_user, password=db_pass)
		
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return db_conn



def db_insert(db_conn, url_path, client_ip, date_time):
    cur = db_conn.cursor()
    cur.execute("INSERT INTO blacklisted(url_path, client_ip, date_time) VALUES('%s', '%s', '%s');" % (url_path, client_ip, date_time))
    db_conn.commit()
    cur.close()


def check_ip(db_conn, ip):
    cur = db_conn.cursor()
    cur.execute("SELECT * FROM blacklisted WHERE client_ip = '%s';" % (ip))
    if cur.rowcount >= 1:
        cur.close()
        return True
    else:
        cur.close()
        return False
