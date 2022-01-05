#Endpoints for the Course

from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.models.course_model import Course_model
from app.core.schemas.course_schema import CourseCreate, Course
from app.core.cruds import course_crud
from app.core.data.database import get_db

router = APIRouter()

@router.get("/", response_model=List[Course])
def read_courses(db: Session = Depends(get_db)):
    """
    Retrieve all courses
    """
    courses = course_crud.get_courses(db)
    return courses

@router.get("/{course_id}", response_model=Course)
def read_course(course_id: str, db: Session = Depends(get_db)):
    """
    Retrieve a course
    """
    course = course_crud.get_course(db, course_id)
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@router.post("/", response_model=Course)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    """
    Create a new course
    """
    return course_crud.create_course(db=db, course=course)
