#!/usr/bin/python3

"""
This module contains class definition of a State and
an instance Base = declarative_base():

Requirements:
- State class:
    - inherits from Base
    - links to the MySQL table states
    - class attribute id that represents a column of an
      auto-generated, unique integer, can't be null and is a primary key.
    - class attribute name that represents a column of a string
      with maximum 128 characters and can't be null
- You must use the module SQLAlchemy
- Your script should connect to a MySQL server
  running on localhost at port 3306
- WARNING: all classes who inherit from Base must be imported
  before calling Base.metadata.create_all(engine)
"""


from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """Defines State class and maps it to a database table"""
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    def __repr__(self):
        """
        Displays string representation that can be used to recreate
        object of States class.
        """
        return f"States(id={self.id!r}, name={self.name!r})"
