#!/usr/bin/python3
"""
Creates the State “California” with the City “San Francisco”.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    username, password, dbname = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{dbname}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create new State and City
    new_state = State(name="California")
    new_city = City(name="San Francisco", state=new_state)
    session.add(new_state)
    session.add(new_city)
    session.commit()

    print(f"{new_state.id}")
    print(f"{new_city.id} -> {new_city.name} in {new_city.state.name}")

    session.close()

