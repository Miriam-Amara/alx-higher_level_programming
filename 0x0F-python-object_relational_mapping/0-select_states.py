#!/usr/bin/python3


"""
A module that lists all states from the database hbtn_0e_0_usa

Requirements:
- Module takes 3 arguments: mysql username, mysql password
  and database name (no argument validation needed)

- Must use the module MySQLdb (import MySQLdb)
- Should connect to a MySQL server running on localhost at port 3306
- Results must be sorted in ascending order by states.id
- Results must be displayed as they are in the example below
- Should not be executed when imported
"""

import MySQLdb
import sys


def validate_cmdline_args():
    """
    Validates and extracts command-line arguments for MySQL connection.

    Returns:
        tuple: A tuple containing the username, password, and database name
               if the arguments are valid, otherwise 'None'.
    """
    try:
        username, password, db_name = sys.argv[1:4]
    except Exception as e:
        print(
            "requires 3 command line args: username, password and db_name\n"
            f"{e}"
        )
        return None
    return (username, password, db_name)


def query_db(username, password, db_name, query, filter_value=None):
    """
    Executes a SQL query on a MySQL database and returns the result.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        db_name (str): MySQL database name.
        query (str): The SQL query to execute.

    Returns:
        list: A list of rows fetched from the database if successful,
              otherwise 'None' if there is an error.
    """
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name
        )
    except Exception as e:
        print(f"Error connecting to MySQL server: {e}")
        return None

    try:
        cursor = db.cursor()
        if not filter_value:
            cursor.execute(query)
        else:
            cursor.execute(query, (filter_value,))
        result = cursor.fetchall()
    except Exception as e:
        print(f"Query not successfully executed: {e}")
        return None
    finally:
        try:
            cursor.close()
            db.close()
        except Exception as e:
            print(f"Database not successfully closed: {e}")
            return None

    return result


if __name__ == "__main__":

    query = """
        SELECT *
        FROM states
        ORDER BY id;
    """

    login_info = validate_cmdline_args()
    if not login_info:
        sys.exit(1)

    usrname, passwd, dbname = login_info
    result = query_db(usrname, passwd, dbname, query)
    if result:
        for row in result:
            print(row)
