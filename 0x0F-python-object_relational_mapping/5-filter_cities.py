#!/usr/bin/python3

"""
A script that takes in the name of a state as an argument and
lists all cities of that state, using the database 'hbtn_0e_4_usa'.

Requirements:
- Your script should take 4 arguments: mysql username, mysql password,
  database name and state name (SQL injection free!)

- You must use the module MySQLdb (import MySQLdb)
- Your script should connect to a MySQL server running
  on localhost at port 3306
- Results must be sorted in ascending order by cities.id
- You can use only execute() once
- The results must be displayed as they are in the example below
- Your code should not be executed when imported
"""

import sys


query_db = __import__("0-select_states").query_db

if __name__ == "__main__":
    try:
        username, password, dbname, state_name = sys.argv[1:5]
    except Exception as e:
        print("Expected 4 command line arguments: "
              "username, password, database name and state name"
              )
        sys.exit(1)

    query = """
        SELECT name
        FROM cities
        WHERE state_id = (SELECT id
                            FROM states
                            WHERE name = %s
                        )
        ORDER BY id;
    """
    records = query_db(username, password, dbname, query, state_name)
    if records:
        for row in records:
            print(
                f"{row[0]}\n" if row == records[-1] else f"{row[0]}, ", end=""
                )
