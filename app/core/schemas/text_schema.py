#Text Pydantic object:
# A text is a line from a class. A text has:
# Id = uuid
# Class = Class object
# Line number = int
# Text = string

from pydantic import Field

from .meta import baseSchema

class TextBase(baseSchema):
    line_number: int
    text: str

class TextCreate(TextBase):
    class_id: str = Field(..., min_length=36)

class Text(TextBase):
    id: str
    class Config:
        orm_mode = True

class CorpusText(baseSchema):
    count: int
    class Config:
        orm_mode = True