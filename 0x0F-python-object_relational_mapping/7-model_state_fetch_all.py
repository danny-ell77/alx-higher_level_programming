#!/usr/bin/python3
"""
script that lists all State objects from the database hbtn_0e_6_usa
    - Your script should take 3 arguments: mysql username, mysql password
    and database name
    - uses the module SQLAlchemy
    - imports State and Base from model_state
    - script connects to a MySQL server running on localhost at port 3306
    - Results are sorted in ascending order by states.id
"""

if __name__ == '__main__':
    import sys
    import warnings
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
	
    warnings.filterwarnings('ignore', message=".*'@@SESSION.GTID_EXECUTED' is deprecated.*")
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    s = Session()

    for row in s.query(State).order_by(State.id.asc()):
        print(row.id, end="")
        print(': ', end="")
        print(row.name)
