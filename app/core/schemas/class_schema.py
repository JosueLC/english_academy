#Class Pydantic object:
# A class have:
# Id = uuid
# Name = string
# Description = string
# Course = Course object
# Audio = url string to audio file
# Texts = list of Text objects

from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import uuid4

from course_schema import Course
from texts_schema import Text

class ClassBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = Field(None, min_length=1, max_length=255)

class ClassCreate(ClassBase):
    pass

class Class_(ClassBase):
    id: str
    course: Course
    audio: str
    texts: List[Text] = Field(default_factory=list)
    class Config:
        orm_mode = True