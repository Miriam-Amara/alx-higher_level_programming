#!/usr/bin/python3

"""
A script that changes the name of a State object
from the database hbtn_0e_6_usa

Requirements:
- Your script should take 3 arguments:
  mysql username, mysql password and database name
- You must use the module SQLAlchemy
- You must import State and Base from model_state -
  from model_state import Base, State
- Your script should connect to a MySQL server running
  on localhost at port 3306
- Change the name of the State where id = 2 to New Mexico
- Your code should not be executed when imported
"""


import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(
            "Expected 3 command line arguments: "
            "username, password, database name"
            )
        sys.exit(1)

    username, password, dbname = sys.argv[1:4]

    try:
        url = f"mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}"
        engine = create_engine(url, pool_pre_ping=True)
        Base.metadata.create_all(engine)
    except Exception as e:
        print(f"Error connecting to mysql server or database: {e}")
        sys.exit(1)

    try:
        Session = sessionmaker()
        session = Session(bind=engine)
        state_obj = session.query(State).filter(State.id == 2).one()
        state_obj.name = "New Mexico"
        session.commit()
    except TypeError as e:
        session.rollback()
        print(f"Query not successfully executed: {e}")
        sys.exit(1)
    finally:
        try:
            session.close()
        except Exception as e:
            print(f"Database was not closed successfully: {e}")
