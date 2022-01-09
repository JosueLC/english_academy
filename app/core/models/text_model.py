#Model for texts object
# A text is a collection of sentences. Each sentence has:
# Id = uuid
# Class = relationship to Class object
# Line number = int
# Text = string

from uuid import uuid4
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.data.database import Base

class Text_model(Base):
    __tablename__ = 'texts'
    id = Column(String(36), primary_key=True, default=str(uuid4()))
    class_id = Column(String(36), ForeignKey('classes.id'))
    class_ = relationship('Class_model', back_populates='texts')
    line_number = Column(int, nullable=False)
    text = Column(String(255), nullable=False)