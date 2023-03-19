#!/usr/bin/python3
"""
This module takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
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
    value = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database)
    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC;".format(value)
    )

    results = cursor.fetchall()

    for row in results:
        print(row)
