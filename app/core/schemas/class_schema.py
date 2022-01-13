#Class Pydantic object:
# A class have:
# Id = uuid
# Name = string
# Description = string
# Course = Course object
# Audio = url string to audio file
# Texts = list of Text objects

from pydantic import Field
from typing import Optional

from .meta import baseSchema
from .text_schema import Text

class ClassBase(baseSchema):
    name: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = Field(None, min_length=1, max_length=255)

class ClassCreate(ClassBase):
    course_id: str = Field(..., min_length=36)
    audio: str = Field(..., min_length=5)

class Class_(ClassCreate):
    id: str
    texts: list[Text] = Field(default_factory=list)
    class Config:
        orm_mode = True

class Class_Out(baseSchema):
    id: str
    name: str
    course_id: str
    class Config:
        orm_mode = True