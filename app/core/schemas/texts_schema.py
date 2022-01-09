#Text Pydantic object:
# A text is a line from a class. A text has:
# Id = uuid
# Class = Class object
# Line number = int
# Text = string

from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import uuid4

from class_schema import Class_

class TextBase(BaseModel):
    line_number: int
    text: str

class TextCreate(TextBase):
    pass

class Text(TextBase):
    id: str
    class_: Class_
    class Config:
        orm_mode = True