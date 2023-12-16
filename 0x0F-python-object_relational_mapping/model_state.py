#!/usr/bin/python3
"""It define State and instance Base = declarative_base():
State class: 
inherits from Base
It inks to the MySQL table states
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base(

class State(Base):
    """It Represents state for MySQL database.
"""
id = Column(Integer, primary_key=True)
nm = Column(String(128), nullable=False)

