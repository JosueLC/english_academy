#SQLAlchemy class model.
# A class have:
# Id = uuid
# Name = string
# Description = string
# Course = Course object
# Audio = url string to audio file
# Texts = list of Text objects

from uuid import uuid4
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.data.database import Base

class Class_model(Base):
    __tablename__ = 'classes'
    id = Column(String(36), primary_key=True, default=str(uuid4()))
    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    course_id = Column(String(36), ForeignKey('courses.id'))
    course = relationship('Course_model', back_populates='classes')
    audio = Column(String(255), nullable=False)
    texts = relationship('Text_model', back_populates='class')
    