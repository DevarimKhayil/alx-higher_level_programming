#!/usr/bin/python3
"""
This script lists all cities along with their state names from the database `hbtn_0e_4_usa`.
The results are sorted in ascending order by city IDs.
"""

import MySQLdb
import sys

def list_cities(username, password, dbname):
    """
    Connects to a MySQL database and lists all cities with their state names,
    sorted by city IDs.
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=dbname)
    cur = db.cursor()
    # Join cities and states to get city names with the corresponding state names
    cur.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) == 4:
        list_cities(sys.argv[1], sys.argv[2], sys.argv[3])

