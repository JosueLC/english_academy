#Router with endpoints to Course Model
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.data.database import get_db
from app.core.schemas.course_schema import CourseCreate, Course, CourseOut
from app.core.cruds import course_crud

router = APIRouter(
    prefix="/course",
    tags=["course"]
)

@router.post("/",response_model=Course)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    db_course = course_crud.get_course_by_name(db, course.name)
    if db_course:
        raise HTTPException(status_code=400, detail="Course already registered")
    return course_crud.create_course(db=db, course=course)

@router.get("/",response_model=list[CourseOut],response_model_exclude_unset=True)
def read_courses(skip: int= 0, limit: int = 100, db: Session = Depends(get_db)):
    return course_crud.get_courses(db=db,skip=skip,limit=limit)

@router.get("/{course_id}", response_model=Course)
def read_course(course_id: str, db: Session = Depends(get_db)):
    db_course = course_crud.get_course(db=db, course_id=course_id)
    if db_course:
        return db_course
    raise HTTPException(status_code=404, detail="Course not found")
