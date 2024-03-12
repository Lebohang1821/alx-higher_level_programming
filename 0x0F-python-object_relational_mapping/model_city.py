#!/usr/bin/python3
"""
It defines city
Inherits from SQLAlchemy Base and links to MySQL table cities
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """It represents city for MySQL database.

    Attributes:
        id (str): City's id.
        name : City's name.
        state_id (sqlalchemy.String): City's state id.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
