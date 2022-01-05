#SQLAlchemy Course Model.
# A course have:
# Id = uuid
# Name = string
# Description = string
# Classes = List of class objects

from uuid import uuid4
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from app.core.data.database import Base

class Course_model(Base):
    __tablename__ = 'courses'
    id = Column(String(36), primary_key=True, default=str(uuid4()))
    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    classes = relationship('Class', back_populates='course')