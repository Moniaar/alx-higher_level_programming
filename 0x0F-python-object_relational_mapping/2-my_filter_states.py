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
    PASS = argv[2]
    DB = argv[3]
    state_name = argv[4]
    db = MySQLdb.connect(host=HOST,
                         port=PORT,
                         user=USER,
                         passwd=PASS,
                         db=DB,
                         charset="utf8")

    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = BINARY '{}' ORDER BY states.id"
    cursor.execute(query.format(state_name))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
