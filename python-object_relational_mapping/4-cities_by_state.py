#!/usr/bin/python3
"""
This module lists all cities from the database `hbtn_0e_4_usa` along with
their state names. The cities are listed in ascending order by their IDs.
The script uses MySQLdb to connect to the database and execute the query.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Ensure the script doesn't execute when imported
    # Connect to the MySQL database using credentials provided as arguments
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3])

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Execute the query to retrieve all cities and their state names
    # Join the cities and states tables on the state_id
    # Order the results by cities.id in ascending order
    cur.execute("SELECT cities.id, cities.name, states.name "
                "FROM cities "
                "JOIN states ON cities.state_id = states.id "
                "ORDER BY cities.id ASC")

    # Fetch all the results of the query
    query_rows = cur.fetchall()

    # Print each row, displaying the city ID, city name, and state name
    for row in query_rows:
        print(row)

    # Close the cursor and connection to the database
    cur.close()
    db.close()
