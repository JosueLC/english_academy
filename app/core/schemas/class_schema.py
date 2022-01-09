#Pydantic Schema for Class Model
from typing import Optional
from pydantic import BaseModel, Field

class ClassBase(BaseModel):
    name: str
    course: str
    level: str

class ClassCreate(ClassBase):
    pass

class Class(ClassBase):
    id: str
    text: str
    audio: str
    class Config:
        orm_mode = True