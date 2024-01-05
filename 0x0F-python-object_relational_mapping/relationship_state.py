#!/usr/bin/python3
"""
It creates State 'California' with City 'San Francisco'
from database hbtn_0e_100_usa: (100-relationship_states_cities.py)
"""
from sqlalchemy import Column, Integer, String
from relationship_city import Base, City
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


class State(Base):
    """It represents state for a MySQL database
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
