#!/usr/bin/python3

"""
a script that lists all cities from the database hbtn_0e_4_usa

Requirements:
- Your script should take 3 arguments:
  mysql username, mysql password and database name

- You must use the module MySQLdb (import MySQLdb)
- Your script should connect to a MySQL server running
  on localhost at port 3306
- Results must be sorted in ascending order by cities.id
- You can use only execute() once
- Results must be displayed as they are in the example below
- Your code should not be executed when imported
"""

import sys


query_db = __import__("0-select_states").query_db

if __name__ == "__main__":
    try:
        username, password, dbname = sys.argv[1:4]
    except Exception:
        print("Expected 3 command line arguments: "
              "username, password, database name"
              )
        sys.exit(1)

    query = """
            SELECT cities.id, cities.name, states.name
            FROM cities
            LEFT JOIN
            states ON cities.state_id = states.id
            ORDER BY id;
            """
    records = query_db(username, password, dbname, query)
    if records:
        for row in records:
            print(row)
