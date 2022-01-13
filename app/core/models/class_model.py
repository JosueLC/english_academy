#SQLAlchemy class model.
# A class have:
# Id = uuid
# Name = string
# Description = string
# Course = Course object
# Audio = url string to audio file
# Texts = list of Text objects

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.models import Base, uuid_generator

class Class_model(Base):
    __tablename__ = 'classes'
    id = Column(String(36), primary_key=True, default=uuid_generator)
    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=True)
    course_id = Column(String(36), ForeignKey('courses.id'))
    audio = Column(String(255), nullable=False)
    
    course = relationship('Course_model', back_populates='classes')
    texts = relationship('Text_model', back_populates='class_')
    