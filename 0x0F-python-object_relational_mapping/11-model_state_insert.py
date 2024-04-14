#!/usr/bin/python3
"""
This script adds the State object 'Louisiana' to the database `hbtn_0e_6_usa`
and prints the new state's id.
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

    # Create new State object
    new_state = State(name="Louisiana")

    # Add the new state to the session
    session.add(new_state)

    # Commit the session to the database
    session.commit()

    # Print the new state's id
    print(new_state.id)

    # Close the session
    session.close()

