#!/usr/bin/python3

"""
A script that lists all State objects that contain the letter a
from the database hbtn_0e_6_usa.

Requirements:
- Your script should take 3 arguments:
  mysql username, mysql password and database name
- You must use the module SQLAlchemy
- You must import State and Base from model_state -
  from model_state import Base, State
- Your script should connect to a MySQL server
  running on localhost at port 3306
- Results must be sorted in ascending order by states.id
- The results must be displayed as they are in the example below
- Your code should not be executed when imported
"""


import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    try:
        username, password, dbname = sys.argv[1:4]
    except Exception:
        print(
            "Expected 3 command line arguments: "
            "username, password, database name"
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
        state_objects = (
            session.query(State).filter(State.name.like("%a%")).all()
            )
        session.close()
    except Exception as e:
        print(f"Query not successfully executed: {e}")
        sys.exit(1)

    for state in state_objects:
        print(f"{state.id}: {state.name}")
