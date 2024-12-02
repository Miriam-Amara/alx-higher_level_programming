#!/usr/bin/python3

"""
A module that lists all states from the database hbtn_0e_0_usa

Requirements: 
Your script should take 3 arguments: mysql username,
mysql password and database name (no argument validation needed)

You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported
"""


from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine,Column, Integer, String
import sys

Base = declarative_base()

class States(Base):
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String)

    def __str__(self):
        return f"({self.id!r}, {self.name!r})"

    def __repr__(self):
        return f"States(id={self.id!r}, name={self.name!r})"
    

mysql_usrname, mysql_passwd, db_name = sys.argv[1:4]

url = f"mysql+mysqldb://{mysql_usrname}:{mysql_passwd}@localhost:3306/{db_name}"
engine = create_engine(url)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

states_records = session.query(States).order_by(States.id).all()
for record in states_records:
    print(record)

