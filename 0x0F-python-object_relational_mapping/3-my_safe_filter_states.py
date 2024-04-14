#!/usr/bin/python3
"""
This module securely filters states in the `hbtn_0e_0_usa` database by a user-provided name
using parameterized SQL queries to avoid SQL injection, and ensures unique output.
"""

import MySQLdb
import sys

def safe_filter_states(username, password, dbname, search_name):
    """
    Connects to a MySQL database and lists all unique states where the name matches
    the user-provided 'search_name' argument, sorted by state id.
    This function uses parameterized queries to prevent SQL injection and a set to ensure uniqueness.
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=dbname)
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (search_name,))
    rows = cur.fetchall()
    seen = set()  # To keep track of seen state names
    for row in rows:
        if row[1] not in seen:
            print(row)
            seen.add(row[1])  # Add to seen to prevent future prints
    cur.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) == 5:
        safe_filter_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

