#!/usr/bin/python3
"""
It lists all states with name starting with N from database hbtn_0e_0_usa
mysql username, mysql password and database name
module MySQLdb (import MySQLdb)
"""
import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database name>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        db = MySQLdb.connect(user=username, passwd=password, db=database)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM `states` WHERE `name` LIKE 'N%' ORDER BY `id`")
        states_starting_with_n = cursor.fetchall()

        for state in states_starting_with_n:
            print(state)

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))

    finally:
        cursor.close()
        db.close()
