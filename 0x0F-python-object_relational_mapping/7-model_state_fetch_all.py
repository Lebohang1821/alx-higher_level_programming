#!/usr/bin/python3
"""
It ists * State objects from database hbtn_0e_6_usa
"""
import sys
from sqlalchemy.orm import sessionmaker
from model_state import State
from sqlalchemy import create_engine

if __name__ == "__main__":
    engn = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Ses = sessionmaker(bind=engn)
    ses = Ses()

    for state in ses.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
