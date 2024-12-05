#!/usr/bin/python3

"""
A script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa:

- Takes 3 arguments: mysql username, mysql password and
  database name (no argument validation needed)

- You must use the module MySQLdb (import MySQLdb)
- Should connect to a MySQL server running on localhost at port 3306
- Results must be sorted in ascending order by states.id
- Results must be displayed as they are in the example below
- Your code should not be executed when imported
"""

import sys


validate_cmdline_args = __import__("0-select_states").validate_cmdline_args
query_db = __import__("0-select_states").query_db

if __name__ == "__main__":

    query = """
            SELECT *
            FROM states
            WHERE BINARY name LIKE "N%"
            ORDER BY id;
            """
    mysql_login = validate_cmdline_args()
    if not mysql_login:
        sys.exit(1)

    username, password, dbname = mysql_login
    records = query_db(username, password, dbname, query)
    if records:
        for row in records:
            print(row)
