#!/usr/bin/python3
"""
This script takes the name of a state as an argument and lists all cities of that state from the database `hbtn_0e_4_usa`.
It ensures the query is safe from SQL injection by using parameterized inputs.
"""

import MySQLdb
import sys

def list_cities_by_state(username, password, dbname, state_name):
    """
    Connects to a MySQL database and lists all cities of a given state,
    sorted by city IDs, using a safe query to prevent SQL injection.
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=dbname)
    cur = db.cursor()
    # Prepare the SQL query using a parameterized placeholder for the state name
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cur.execute(query, (state_name,))
    rows = cur.fetchall()
    # Join fetched city names with a comma and space
    if rows:
        print(", ".join([city[0] for city in rows]))
    cur.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) == 5:
        list_cities_by_state(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

