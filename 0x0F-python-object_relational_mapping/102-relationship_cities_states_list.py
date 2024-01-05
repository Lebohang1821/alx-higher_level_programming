#!/usr/bin/python3
"""
It lists all City objects from database hbtn_0e_101_usa
---It use module SQLAlchemy
--- It must be displayed as they are in example below
---It take 3 arguments:
---- mysql username, mysql password and database name
"""
import sys
from sqlalchemy import create_engine
from relationship_city import City
from relationship_state import State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for city in session.query(City).order_by(City.id):
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
