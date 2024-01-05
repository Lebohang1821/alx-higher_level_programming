#!/usr/bin/python3

"""
It creates State “California” with City “San Francisco”
from database hbtn_0e_100_usa: (100-relationship_states_cities.py)
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """It epresents city for a MySQL database
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
