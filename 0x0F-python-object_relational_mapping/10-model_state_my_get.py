#!/usr/bin/python3
"""
This script prints the ID of the State object with the specified name from the database `hbtn_0e_6_usa`.
If no state with the given name exists, it prints 'Not found'.
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
    state_name_to_search = sys.argv[4]

    # Create an engine
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{database}')

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query for the state with the given name, using parameterized input to avoid SQL injection
    state = session.query(State).filter(State.name == state_name_to_search).first()

    # Check if the state was found and print the appropriate result
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()

