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
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    # Create a cursor object
    with db.cursor() as cur:
        cur.execute("""
            SELECT
                *
            FROM
                states
            WHERE
                name LIKE BINARY %(name)s
            ORDER BY
                states.id ASC
        """, {
            'name': argv[4]
        })
        # Fetch all the results of the query
        rows = cur.fetchall()
    # Print each row
    if rows is not None:
        for row in rows:
            print(row)

    # Close the cursor and connection to the database
    cur.close()
    db.close()
