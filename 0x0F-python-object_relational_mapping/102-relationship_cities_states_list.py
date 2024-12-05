#!/usr/bin/python3

"""
A script that lists all City objects from the database hbtn_0e_101_usa

Requirements:
- Your script should take 3 arguments:
  mysql username, mysql password and database name
- You must use the module SQLAlchemy
- Your script should connect to a MySQL server running
  on localhost at port 3306
- You must use only one query to the database
- You must use the state relationship to access to
   the State object linked to the City object
- Results must be sorted in ascending order by cities.id
- Results must be displayed as they are in the example below
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
        print(f"Error connecting to mysql server: {e}")
        sys.exit(1)

    Session = sessionmaker()
    session = Session(bind=engine)
    cities = session.query(City).all()

    for city in cities:
        print(f"{city.id}: {city.name} -> {city.states.name}")

    session.close()
