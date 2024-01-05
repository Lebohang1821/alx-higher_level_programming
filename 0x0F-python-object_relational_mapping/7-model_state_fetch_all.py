#!/usr/bin/python3
"""
It  lists all State objects from database hbtn_0e_6_usa
It take 3 arguments: mysql username, mysql password and database name
It import State and Base from model_state - from model_state
import Base, State
"""
import sys
from sqlalchemy.orm import sessionmaker
from model_state import State
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
