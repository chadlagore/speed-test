import json
import psycopg2

from get_speed import execute_syscall

conn = psycopg2.connect(
    "dbname='speed_test' user='postgres' host='localhost' password='emerald3'"
    )

def get_response():
#    resp = execute_syscall()
    with open('cache.json', 'r') as infile:
        resp = json.load(infile)
    return resp

def update_record():
    cur = conn.cursor()
    query =  "INSERT INTO wifi_speed(date, download, upload, ping, latency, url, sponsor) VALUES (%s, %s, %s);"
    data = (info, city, price)
    cursor.execute(query, data)
    conn.commit()

def main():
    get_response()

if __name__ == '__main__':
    main()
