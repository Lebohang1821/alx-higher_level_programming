#!/usr/bin/python3
"""
It lists all states with name starting with N from database hbtn_0e_0_usa
mysql username, mysql password and database name
module MySQLdb (import MySQLdb)
"""
import MySQLdb
import sys

if __name__ == "__main__":
"starting point"
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states` ORDER BY `id`")
    [print(state) for state in c.fetchall() if state[1][0] == "N"]
