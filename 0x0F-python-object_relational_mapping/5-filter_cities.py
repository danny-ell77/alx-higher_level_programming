#!/usr/bin/python3
"""
This module takes in the name of a state as an argument and 
lists all cities of that state, using the database hbtn_0e_4_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    value = sys.argv[4]

    db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database)
    cursor = db.cursor()

    cursor.execute(
        "SELECT c.`name` FROM `cities` AS c INNER JOIN `states` AS s ON c.`state_id` = s.`id` WHERE s.`name` = %s ORDER BY c.`id`;",
        (value,),
    )

    results = cursor.fetchall()

    for row in results:
        print(row, end=", ")
