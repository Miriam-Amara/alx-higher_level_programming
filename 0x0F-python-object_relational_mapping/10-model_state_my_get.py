#!/usr/bin/python3

"""
A script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa.

Requirements:
- Your script should take 4 arguments: mysql username, mysql password,
  database name and state name to search (SQL injection free)
- You must use the module SQLAlchemy
- You must import State and Base from model_state -
  from model_state import Base, State
- Your script should connect to a MySQL server
  running on localhost at port 3306
- You can assume you have one record with the state name to search
- Results must display the states.id
- If no state has the name you searched for, display Not found
- Your code should not be executed when imported
"""


import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    try:
        username, password, dbname, state_name = sys.argv[1:5]
    except Exception as e:
        print(
            "Expected 4 command line arguments: "
            f"username, password, database name, state name\n{e}"
            )
        sys.exit(1)

    try:
        url = f"mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}"
        engine = create_engine(url, pool_pre_ping=True)
        Base.metadata.create_all(engine)
    except Exception as e:
        print(f"Error connecting to mysql server: {e}")
        sys.exit(1)

    Session = sessionmaker()
    session = Session(bind=engine)

    try:
        state_obj = (
            session.query(State).filter(State.name == state_name).first()
            )
        session.close()
    except Exception as e:
        print(f"Query not successfully executed: {e}")
        sys.exit(1)

    if state_obj:
        print(state_obj.id)
    else:
        print("Not found")
