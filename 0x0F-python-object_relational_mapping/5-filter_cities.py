#!/usr/bin/python3
"""Script to list all cities of a state from the database hbtn_0e_4_usa."""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    # Check if correct number of arguments are provided
    if len(argv) != 5:
        print("Usage: {} <mysql_username> <mysql_password> <database_name> <state_name>"
              .format(argv[0]))
        exit(1)

    # Get MySQL credentials and state name from command line arguments
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]
    state_name = argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username, passwd=mysql_password, db=database_name)
    cursor = db.cursor()

    # Execute the SQL query to retrieve all cities of the specified state
    query = """
            SELECT cities.id, cities.name, states.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id
            """
    cursor.execute(query, (state_name,))

    # Fetch all the rows
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
