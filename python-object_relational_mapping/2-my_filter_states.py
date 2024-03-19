#!/usr/bin/python3
"""
This module takes in an argument and displays all values in the
`states` table of `hbtn_0e_0_usa` where `name` matches the argument.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3])

    # Create a cursor object
    cur = db.cursor()

    # Form the SQL query with the user input
    query = ("SELECT * FROM states WHERE name = '{}' "
             "ORDER BY id ASC").format(argv[4])

    # Execute the query
    cur.execute(query)

    # Fetch all the results of the query
    rows = cur.fetchall()

    # Print each row
    for row in rows:
        if row[1] == argv[4]:
            print(row)

    # Close the cursor and connection to the database
    cur.close()
    db.close()
