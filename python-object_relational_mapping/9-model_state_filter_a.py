#!/usr/bin/python3
"""
This script lists all State objects that contain the letter 'a'
from the database `hbtn_0e_6_usa`.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    # Create engine
    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}: '
                           f'{sys.argv[2]}@localhost/{sys.argv[3]}',
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query States containing 'a'
    states = session.query(State).filter(State.name.like('%a%'))\
        .order_by(State.id)

    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()
