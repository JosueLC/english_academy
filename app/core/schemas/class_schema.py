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
    pass

class Class_(ClassBase):
    id: str
    course_id: str = Field(..., min_length=36)
    audio: str
    texts: list[Text] = Field(default_factory=list)
    class Config:
        orm_mode = True