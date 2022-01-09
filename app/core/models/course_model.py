#Course object:
# A course is a collection of classes. A course has:
# Id = uuid
# Name = string
# Description = string
# Classes = list of Class objects

from uuid import uuid4
from sqlalchemy import Column, String, Integer,ForeignKey
from sqlalchemy.orm import relationship
from app.core.data.database import Base

class Course_model(Base):
    __tablename__ = 'courses'
    id = Column(String(36), primary_key=True, default=str(uuid4()))
    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    classes = relationship('Class_model', back_populates='course')
    level = Column(Integer, nullable=False)