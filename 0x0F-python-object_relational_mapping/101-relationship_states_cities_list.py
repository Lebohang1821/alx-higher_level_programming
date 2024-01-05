#!/usr/bin/python3
"""
 It lists * State objects, and corresponding City objects
 __contained in database hbtn_0e_101_usaIt
 -It must be sorted in ascending order by states.id and cities.id
 --It must be displayed as they are in example below
"""
import sys
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
