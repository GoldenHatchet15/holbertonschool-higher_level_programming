#!/usr/bin/python3
"""
This module takes in an argument and displays all values in the
`states` table of `hbtn_0e_0_usa` where `name` matches the argument,
safeguarding against SQL injection.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3])

    # Create a cursor object
    cur = db.cursor()

    # Prepare a parameterized query
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    # Execute the query with the user input as a parameter
    cur.execute(query, (argv[4],))

    # Fetch all the results of the query
    rows = cur.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close the cursor and connection to the database
    cur.close()
    db.close()
