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


from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine, Column, Integer, String
import sys

Base = declarative_base()


class States(Base):
    """Defines States class and maps it to a database table"""
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String)

    def __str__(self):
        """
        Displays user-friendly string representation of States objects
        """
        return f"({self.id!r}, {self.name!r})"

    def __repr__(self):
        """
        Displays string representation that can be used to recreate
        object of States class.
        """
        return f"States(id={self.id!r}, name={self.name!r})"


mysql_usrname, mysql_passwd, db_name = sys.argv[1:4]

url = (
    f"mysql+mysqldb://{mysql_usrname}:{mysql_passwd}@localhost:3306/{db_name}"
    )
engine = create_engine(url)
Base.metadata.create_all(engine)

if __name__ == "__main__":
    Session = sessionmaker(bind=engine)
    session = Session()

    states_records = session.query(States).order_by(States.id).all()
    for record in states_records:
        print(record)
