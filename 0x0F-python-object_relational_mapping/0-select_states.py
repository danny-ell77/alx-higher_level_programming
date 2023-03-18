#!/usr/bin/python3
"""
This module lists all states from the database hbtn_0e_0_usa
Arguments:
    mysql username (str)
    mysql password (str)
    database name (str)
"""
import sys
import MySQLdb


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database)
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC;")

    results = cursor.fetchall()

    for row in results:
        print(row)
