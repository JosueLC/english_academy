#CRUD for Course Model
from sqlalchemy.orm import Session

from ..models.course_model import Course_model
from ..schemas.course_schema import CourseCreate

def get_course(db: Session, course_id: str):
    return db.query(Course_model).filter(Course_model.id == course_id).first()

def get_course_by_name(db: Session, course_name: str):
    return db.query(Course_model).filter(Course_model.name == course_name).first()

def get_courses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Course_model).offset(skip).limit(limit).all()

def create_course(db: Session, course: CourseCreate):
    db_course = Course_model(name=course.name, description = course.description, level = course.level)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course