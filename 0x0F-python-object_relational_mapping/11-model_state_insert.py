#!/usr/bin/python3
"""Script to add the State object "Louisiana" to the database hbtn_0e_6_usa."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    # Check if correct number of arguments are provided
    if len(argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>"
              .format(argv[0]))
        exit(1)

    # Get MySQL credentials from command line arguments
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]

    # Create an engine to connect to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(mysql_username, mysql_password,
                                   database_name))

    # Bind the engine to the Base class
    Base.metadata.bind = engine

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Add the State object "Louisiana" to the database
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # Print the new states.id after creation
    print(new_state.id)

    # Close the session
    session.close()

