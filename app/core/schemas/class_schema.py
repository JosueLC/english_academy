#Pydantic Schema for Class Model
from typing import Optional
from pydantic import BaseModel, Field

class ClassBase(BaseModel):
    name: str
    description: str

class ClassCreate(ClassBase):
    pass

class Class(ClassBase):
    id: str
    content: str
    audio: str
    class Config:
        orm_mode = True