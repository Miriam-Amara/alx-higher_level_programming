#!/usr/bin/python3

"""
A script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.

Requirements:
- Your script should take 4 arguments:
  mysql username, mysql password, database name and
  state name searched (no argument validation needed)

- You must use the module MySQLdb (import MySQLdb)
- Should connect to a MySQL server running on localhost at port 3306
- You must use format to create the SQL query with the user input
- Results must be sorted in ascending order by states.id
- Results must be displayed as they are in the example below
- Your code should not be executed when imported
"""

import sys


query_db = __import__("0-select_states").query_db

if __name__ == "__main__":
    try:
        username, password, dbname, filter_value = sys.argv[1:5]
    except Exception:
        print("Expected 4 command line arguments: "
              "username, password, database name and state name"
              )
        sys.exit(1)

    query = """
            SELECT *
            FROM states
            WHERE name = "{}"
            ORDER BY id;
            """.format(filter_value)
    records = query_db(username, password, dbname, query)
    if records:
        for row in records:
            print(row)
