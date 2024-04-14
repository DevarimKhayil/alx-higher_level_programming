#!/usr/bin/python3
"""
This module defines a State model.
It sets up a mapping to a MySQL table 'states', containing 'id' and 'name' fields.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """Represents a state for a MySQL database.

    __tablename__ : str
        The name of the MySQL table to store states.
    id : Integer
        State's unique identifier, autoincrements and is the primary key. Cannot be null.
    name : String
        State's name, must be a string of maximum 128 characters. Cannot be null.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

