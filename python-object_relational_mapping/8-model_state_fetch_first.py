#!/usr/bin/python3
"""
This script prints the first State object from the database `hbtn_0e_6_usa`.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    # Connect to the given database URL
    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:'
                           f'{sys.argv[2]}@localhost/{sys.argv[3]}',
                           pool_pre_ping=True)
    # Bind the engine to the metadata of the Base class
    Base.metadata.create_all(engine)

    # Create a DBSession instance
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the first State object by its ID
    state = session.query(State).order_by(State.id).first()

    # Print the state if it exists, otherwise print 'Nothing'
    if state:
        print(f"{state.id}: {state.name}")
    else:
        print("Nothing")

    session.close()
