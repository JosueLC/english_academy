#Router to Class Object
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.data.database import get_db
from app.core.schemas.class_schema import ClassCreate, Class_
from app.core.cruds import class_crud, course_crud

router = APIRouter(
    prefix="/class",
    tags=["class"]
)

@router.post("/",response_model=Class_)
def create_class(classs:ClassCreate, db: Session = Depends(get_db)):
    db_class = class_crud.get_class_by_name(db, classs.name)
    if db_class:
        raise HTTPException(status_code=400, detail="Class already registered")
    db_course = course_crud.get_course(db, classs.course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course parent not found")
    return class_crud.create_class(db=db, class_=classs)

@router.get("/course/{course_id}",response_model=list[Class_])
def read_classes_by_curse(course_id: str, db: Session = Depends(get_db)):
    db_course = course_crud.get_course(db, course_id)
    if db_course:
        return class_crud.get_classes_by_course(db, course_id)
    raise HTTPException(status_code=404, detail="Course parent not found")

@router.get("/{class_id}", response_model=Class_)
def read_class(class_id, db: Session = Depends(get_db)):
    db_class = class_crud.get_class(db, class_id)
    if db_class:
        return db_class
    raise HTTPException(status_code=404, detail="Class not found")