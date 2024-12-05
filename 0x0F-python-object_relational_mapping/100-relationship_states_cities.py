#!/usr/bin/python3

"""
A script that creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa.

Requirements:
- Your script should take 3 arguments:
  mysql username, mysql password and database name
- You must use the module SQLAlchemy
- Your script should connect to a MySQL server running
  on localhost at port 3306
- You must use the cities relationship for all State objects
- Your code should not be executed when imported
"""


import sys
from relationship_state import Base, State
from relationship_city import City
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
    
    Session = sessionmaker()
    session = Session(bind=engine)
    state_obj = State(name="California")
    city_obj = City(name="San Francisco")
    city_obj.states = state_obj
    session.add(state_obj)
    session.commit()
    session.close()
