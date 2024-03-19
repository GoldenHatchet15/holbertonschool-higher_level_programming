#!/usr/bin/python3
"""
This script deletes all State objects with a name containing the letter 'a'
from the database `hbtn_0e_6_usa`.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    # Connect to the given database URL
    engine = create_engine(
        f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}',
        pool_pre_ping=True
    )

    # Bind the engine to the metadata of the Base class
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for all State objects with a name containing the letter 'a'
    states_to_delete = {
        session.query(State).filter(State.name.like('%a%')).all()
    }

    # Delete those objects
    for state in states_to_delete:
        session.delete(state)

    # Commit the changes
    session.commit()

    session.close()
