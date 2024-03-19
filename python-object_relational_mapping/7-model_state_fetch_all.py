#!/usr/bin/python3
"""
This script lists all State objects from the database `hbtn_0e_6_usa`.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Create an engine that connects to the given database URL
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Bind the engine to the metadata of the Base class
    Base.metadata.create_all(engine)

    # Create a Session class with the engine
    Session = sessionmaker(bind=engine)

    # Instantiate a Session
    session = Session()

    # Query for all State objects, order them by id
    states = session.query(State).order_by(State.id.asc()).all()

    # Iterate through the list of states and print them
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
