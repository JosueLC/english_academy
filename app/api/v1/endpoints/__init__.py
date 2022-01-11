from .course_end import router as course
from .class_end import router as classs
from .text_end import router as text

endpoints = [
    course,
    classs,
    text
]