#!/usr/bin/python3
"""
script that lists all states from the database
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    database = argv[3]
    db = MySQLdb.connect(host="localhost", port=3306, user=user,
                         passwd=passwd, db=database)

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()

