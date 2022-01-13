from uuid import uuid4
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def uuid_generator():
    return str(uuid4())