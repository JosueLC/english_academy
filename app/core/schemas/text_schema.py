#Text Pydantic object:
# A text is a line from a class. A text has:
# Id = uuid
# Class = Class object
# Line number = int
# Text = string

from pydantic import BaseModel, Field

class TextBase(BaseModel):
    line_number: int
    text: str

class TextCreate(TextBase):
    pass

class Text(TextBase):
    id: str
    class_id: str = Field(..., min_length=36)
    class Config:
        orm_mode = True