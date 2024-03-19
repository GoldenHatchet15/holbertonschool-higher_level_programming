#!/usr/bin/python3
"""
A script that lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

def main():
    # Unpack command line arguments
    mysql_username, mysql_password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                         passwd=mysql_password, db=db_name, charset="utf8")
    cur = db.cursor()
    
    # Execute the query
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    
    # Fetch all the results
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    
    # Close the cursor and the connection
    cur.close()
    db.close()

if __name__ == "__main__":
    main()
