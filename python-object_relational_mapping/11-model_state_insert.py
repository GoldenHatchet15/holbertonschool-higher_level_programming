#!/usr/bin/python3
"""
This script adds the State object "Louisiana" to the database `hbtn_0e_6_usa`
and prints the new state's ID after creation.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    # Connect to the given database URL
    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}: '
                           f'{sys.argv[2]}@localhost/{sys.argv[3]}',
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new State object for "Louisiana"
    new_state = State(name="Louisiana")

    # Add the new State object to the session and commit the changes
    session.add(new_state)
    session.commit()

    # Print the new state's ID
    print(new_state.id)

    session.close()
