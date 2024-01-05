#!/usr/bin/python3
"""
It Creates State 'California' with the City 'San Francisco'
from the database hbtn_0e_100_usa.
---It Improve the files model_city.py and model_state.py
---3 arguments: mysql username, mysql password and database name
---It use the module SQLAlchemy
"""
import sys
from relationship_state import State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_city import Base, City

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(City(name="San Francisco", state=State(name="California")))
    session.commit()
