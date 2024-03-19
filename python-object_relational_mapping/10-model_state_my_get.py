#!/usr/bin/python3
"""
This script prints the State object with the name passed as an argument
from the database `hbtn_0e_6_usa`. It's SQL injection free.
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

    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State object with the name passed as an argument
    state = session.query(State).filter(State.name == sys.argv[4]).first()

    # Print the state id if found, otherwise print 'Not found'
    if state:
        print(f"{state.id}")
    else:
        print("Not found")

    session.close()
