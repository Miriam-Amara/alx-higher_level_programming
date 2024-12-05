#!/usr/bin/python3

"""
This module contains the class definition of a City.

City class:
- Inherits from Base (imported from model_state)
- Links to the MySQL table cities
- Class attribute id that represents a column of an auto-generated,
  unique integer, can't be null and is a primary key
- Class attribute name that represents a column of a string
  of 128 characters and can't be null
- Class attribute state_id that represents a column of an integer,
  can't be null and is a foreign key to states.id
"""

from relationship_state import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """
    Defines a City object which links
    to the 'cities' table in the database.

    Attributes:
        id (int): The unique identifier for the city.
        name (str): The name of the city.
        state_id (int): The foreign key linking to the 'states' table.

    Relationships:
        state (State): The relationship with the State object.
                        A city is associated with one state.
    """
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

    def __str__(self):
        """
        Returns a user friendly string representation of the city object.
        """
        return f"{self.__class__.__name__}: ({self.id}) {self.name}"

    def __repr__(self):
        """
        Returns a string representation of the City object
        that can be used to recreate it.
        """
        return (
            f"City(id={self.id!r}, name={self.name!r}, "
            f"state_id={self.state_id!r})"
            )
