#!/usr/bin/python3
"""
This script lists all State objects from the database `hbtn_0e_6_usa`.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Extract command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create an engine
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{database}')

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query for all the states in the database
    states = session.query(State).order_by(State.id).all()

    # Print states
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
