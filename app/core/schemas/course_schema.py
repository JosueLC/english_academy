#Course Pydantic object:
# A course is a collection of classes. A course has:
# Id = uuid
# Name = string
# Description = string (optional)
# Classes = list of Class objects

from pydantic import BaseModel, Field
from typing import Optional
from uuid import uuid4

from .class_schema import Class_

class CourseBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = Field(None, min_length=1, max_length=255)

class CourseCreate(CourseBase):
    pass

class Course(CourseBase):
    id: str
    classes: list[Class_] = Field(default_factory=list)
    class Config:
        orm_mode = True