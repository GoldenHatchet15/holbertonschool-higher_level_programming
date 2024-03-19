#!/usr/bin/python3
"""
This module takes the name of a state as an argument and lists all cities
of that state from the database `hbtn_0e_4_usa`, in a safe way that prevents
SQL injection.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3])

    # Create a cursor object
    cur = db.cursor()

    # Form a parameterized query to prevent SQL injection
    query = ("SELECT cities.name "
             "FROM cities "
             "JOIN states ON cities.state_id = states.id "
             "WHERE states.name = %s "
             "ORDER BY cities.id ASC")

    # Execute the query with the user input as a parameter
    cur.execute(query, (argv[4],))

    # Fetch all the results of the query
    query_rows = cur.fetchall()

    # Print the city names in one line
    print(", ".join(city[0] for city in query_rows))

    # Close the cursor and connection to the database
    cur.close()
    db.close()
