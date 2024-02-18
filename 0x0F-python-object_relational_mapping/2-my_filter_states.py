#!/usr/bin/python3
"""A Script that will lists all states from the database hbtn_0e_0_usa
But with the name is mathcing the argument passed! :)
"""


if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    HOST = "localhost"
    PORT = 3306
    USER = argv[1]
    PASSWORD = argv[2]
    DATABASE = argv[3]
    db = MySQLdb.connect(host=HOST,
                         port=PORT,
                         user=USER,
                         passwd=PASSWORD,
                         db=DATABASE,
                         charset="utf8")

    cursor = db.cursor()
    # The query to search for any argument assoiciated with the name as a string
    query = "SELECT * FROM states WHERE name = BINARY '{}' ORDER BY states.id"
    # to check the format of the name of the state that is passed using the format method
    cursor.exectue(query.format(state_name))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
