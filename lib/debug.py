# lib/sqlalchemy_sandbox.py
#!/usr/bin/env python3

#  imports
from sqlalchemy import create_engine
from sqlalchemy_sandbox import Student

# data models

engine = create_engine('sqlite:///students.db')

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    import ipdb; ipdb.set_trace()
