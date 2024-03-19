#!/usr/bin/python3
"""
This module lists all states from the database `hbtn_0e_0_usa` that
start with the letter 'N'. The states are listed in ascending order
by their id.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to the MySQL database
    conn = MySQLdb.connect(host="localhost", user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])

    # Create a cursor object
    cur = conn.cursor()

    # Execute the query to select states starting with 'N'
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all the results of the query
    query_rows = cur.fetchall()

    # Print each row
    for row in query_rows:
        print(row)

    # Close the cursor and connection to the database
    cur.close()
    conn.close()
