#Pydantic Schema for Course Model
from typing import Optional
from pydantic import BaseModel, Field

class CourseBase(BaseModel):
    name: str
    description: str

class CourseCreate(CourseBase):
    pass

class Course(CourseBase):
    id: str
    classes: Optional[list] = Field(None, description='List of classes')
    class Config:
        orm_mode = True