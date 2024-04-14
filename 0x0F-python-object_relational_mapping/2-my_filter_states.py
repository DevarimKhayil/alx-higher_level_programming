#!/usr/bin/python3
import MySQLdb
import sys

def filter_states_by_input(username, password, dbname, state_name):
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=dbname)
    cur = db.cursor()
    query = "SELECT DISTINCT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (state_name,))
    rows = cur.fetchall()
    seen = set()
    for row in rows:
        if row[1] not in seen:
            print(row)
            seen.add(row[1])
    cur.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) == 5:
        filter_states_by_input(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
