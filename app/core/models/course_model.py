#Course object:
# A course is a collection of classes. A course has:
# Id = uuid
# Name = string
# Description = string
# Classes = list of Class objects

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from app.core.models import Base, uuid_generator

class Course_model(Base):
    __tablename__ = 'courses'
    id = Column(String(36), primary_key=True, default=uuid_generator)
    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=True)
    level = Column(Integer, nullable=False)
    
    classes = relationship('Class_model', back_populates='course')