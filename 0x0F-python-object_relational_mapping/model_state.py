#!/usr/bin/python3
"""a python file that contains the class definition of a State
and an instance Base = declarative_base()"""


from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class State(Base):
    """Class representing the states table in MySQL
       id: a column of an auto-generated, unique integer, can’t be null
           and is a primary key
       name: name of every state"""

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

