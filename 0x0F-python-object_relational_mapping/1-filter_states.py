#!/usr/bin/python3
"""
This module lists all unique states with names starting with 'N' from the database `hbtn_0e_0_usa`.
The states are sorted in ascending order by their IDs.
"""

import MySQLdb
import sys

def filter_states(username, password, dbname):
    """
    Connects to a MySQL database and lists all unique states with names starting with 'N'.
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=dbname)
    cur = db.cursor()
    cur.execute("SELECT DISTINCT name FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) == 4:
        filter_states(sys.argv[1], sys.argv[2], sys.argv[3])

