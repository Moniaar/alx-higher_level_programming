#!/usr/bin/python3
"""A script that lists all cities from the database hbtn_0e_4_usa"""

if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    # Check if correct number of arguments are provided
    if len(argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>".format(argv[0]))
        exit(1)

    # Get MySQL credentials from command line arguments
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]

    try:
        # Connect to MySQL server
        db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username, passwd=mysql_password, db=database_name)
        cursor = db.cursor()

        # Execute the SQL query with parameters to retrieve all cities with corresponding state names
        query = "SELECT c.id, c.name, st.name FROM cities c, states st WHERE c.state_id = st.id ORDER BY c.id"
        cursor.execute(query)

        # Fetch all the rows
        rows = cursor.fetchall()

        # Display the results
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("Error connecting to the database:", e)
    finally:
        # Close the database connection
        if db:
            cursor.close()
            db.close()
