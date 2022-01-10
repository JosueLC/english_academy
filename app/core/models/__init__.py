from sqlalchemy.orm import scoped_session, sessionmaker
from .meta import Base

from .course_model import Course_model
from .class_model import Class_model
from .text_model import Text_model

DBSession = scoped_session(sessionmaker())
def initialize_sql(engine):
    DBSession.configure(bind=engine)
    Base.metadata.bind=engine
    Base.metadata.create_all(engine)