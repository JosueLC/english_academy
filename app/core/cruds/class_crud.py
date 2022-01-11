#CRUD for Class Model
from sqlalchemy.orm import Session
from ..models.class_model import Class_model
from ..schemas.class_schema import ClassCreate

def get_class(db: Session, class_id: str):
    return db.query(Class_model).filter(Class_model.id == class_id).first()

def get_class_by_name(db: Session, name: str):
    return db.query(Class_model).filter(Class_model.name == name).first()

def get_classes_by_course(db: Session, course_id: str, skip: int = 0, limit: int = 100):
    return db.query(Class_model).filter(Class_model.course_id == course_id).offset(skip).limit(limit).all()

def get_classes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Class_model).offset(skip).limit(limit).all()

def create_class(db: Session, class_: ClassCreate):
    db_class = Class_model(**class_.dict())
    db.add(db_class)
    db.commit()
    db.refresh(db_class)
    return db_class