#Router to Text Object
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.data.database import get_db
from app.core.schemas.text_schema import TextCreate, Text
from app.core.cruds import text_crud, class_crud

router = APIRouter(
    prefix="/texts",
    tags=["texts"]
)

@router.post("/",response_model=Text)
def create_text(text:TextCreate, db: Session = Depends(get_db)):
    #check that text is not already exists.
    if text_crud.exists(db,text.class_id,text.line_number):
        raise HTTPException(status_code=400, detail="Text already registered")
    #Check if class_id exists
    db_class = class_crud.get_class(db,text.class_id)
    if db_class:
        return text_crud.create_text(db=db,text=text)
    raise HTTPException(status_code=404, detail="Class parent not found")

@router.get("/{class_id}", response_model=list[Text])
def read_texts_by_class(class_id: str, db: Session = Depends(get_db)):
    db_class = class_crud.get_class(db,class_id)
    if db_class:
        return text_crud.get_text_by_class(db,class_id)
    raise HTTPException(status_code=404, detail="Class parent not found")