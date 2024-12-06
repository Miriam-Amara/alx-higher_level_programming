#!/usr/bin/python3

"""
A that prints all City objects from the database hbtn_0e_14_usa

Requirements:
- Your script should take 3 arguments:
  mysql username, mysql password and database name
- You must use the module SQLAlchemy
- You must import State and Base from model_state -
  from model_state import Base, State
- Your script should connect to a MySQL server running
  on localhost at port 3306
- Results must be sorted in ascending order by cities.id
- Results must be display as they are in the example below
  (<state name>: (<city id>) <city name>)
- Your code should not be executed when imported
"""


import sys
from model_state import State
from model_city import Base, City
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

    try:
        Session = sessionmaker()
        session = Session(bind=engine)
        result = (session.query(State.name, City.id, City.name)
                  .join(City, City.state_id == State.id).all())
        session.close()
    except Exception as e:
        print(f"Query not successfully executed: {e}")
        sys.exit(1)

    for row in result:
        state_name, city_id, city_name = row
        print(f"{state_name}: ({city_id}) {city_name}")
