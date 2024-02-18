#!/usr/bin/python3
"""A Script that will lists all states from the database hbtn_0e_0_usa
But with the name starting with N in uppercase
"""

if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    HOST = "localhost"
    PORT = 3306
    USER = argv[1]
    PASS = argv[2]
    DB = argv[3]

    try:
        db = MySQLdb.connect(host=HOST,
                             port=PORT,
                             user=USER,
                             passwd=PASS,
                             db=DB,
                             charset="utf8")

        cursor = db.cursor()

        # The corrected query to search among all states rows
        query = "SELECT * FROM states " \
                "WHERE name LIKE BINARY 'N%' " \
                "ORDER BY id ASC"

        cursor.execute(query)
        rows = cursor.fetchall()

        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("Error connecting to the database:", e)
    finally:
        if db:
            cursor.close()
            db.close()
