#!/usr/bin/python3
"""
It Lists * states from database hbtn_0e_0_usa.
mysql username, mysql password and database name
"""
import MySQLdb
import sys

if __name__ == "__main__":
#It check if correct number of command-line arguments is provided
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    [print(state) for state in c.fetchall()]
