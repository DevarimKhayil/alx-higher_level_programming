#!/usr/bin/python3
"""
This script prints the first State object from the database `hbtn_0e_6_usa`.
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

    # Query for the first state in the database, ordered by id
    first_state = session.query(State).order_by(State.id).first()

    # Print the first state if it exists, otherwise print 'Nothing'
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    # Close the session
    session.close()
