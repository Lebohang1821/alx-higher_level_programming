#!/usr/bin/python3
"""
It lists all State objects that contain letter
a from database hbtn_0e_6_usa
It 3 arguments: mysql username, mysql password and database name
- must be sorted in ascendin order by states.id
--MySQL server running on localhost at port 3306
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id):
        if "a" in state.name:
            print("{}: {}".format(state.id, state.name))
