#!/usr/bin/python3
"""
It defines State model
Inherits from SQLAlchemy Base and links to MySQL table states
It uses use the module SQLAlchemy
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """It epresents state for MySQL database
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
