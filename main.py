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

def update_record(resp):
    cur = conn.cursor()
    query = "INSERT INTO wifi_speed(date, download, upload, ping, latency, url, sponsor) VALUES (%s, %s, %s, %s, %s, %s, %s);"
    data = (
        resp['timestamp'],
        resp['download'],
        resp['upload'],
        resp['ping'],
        resp['server']['latency'],
        resp['server']['url'],
        resp['server']['sponsor'],
        )
    cursor.execute(query, data)
    conn.commit()

def main():
    resp = get_response()
    update_record(resp)

if __name__ == '__main__':
    main()
