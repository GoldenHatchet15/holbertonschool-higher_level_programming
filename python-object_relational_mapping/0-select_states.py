#!/usr/bin/python3
"""
This script lists all states from the
database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Accesses the database and gets the states
    from the database.
    """
    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    # Execute the query
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cur.fetchall()

    # Iterate over and print each row
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()

