#!/usr/bin/python3
"""
It adds State object “Louisiana” to database hbtn_0e_6_usa
mysql username, mysql password and database name
It must use the module SQLAlchemy
It  import State and Base from model_state -
from model_state import Base, State
"""
import sys
from model_state import State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    louisiana = State(name="Louisiana")
    session.add(louisiana)
    session.commit()
    print(louisiana.id)
