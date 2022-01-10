#CRUD for Text Model
from sqlalchemy.orm import Session
from ..models.text_model import Text_model
from ..schemas.text_schema import TextCreate

def get_text(db: Session, text_id: str):
    return db.query(Text_model).filter(Text_model.id == text_id).first()

def get_text_by_class(db: Session, class_id: str, skip: int = 0, limit: int = 100):
    return db.query(Text_model).filter(Text_model.class_id == class_id).offset(skip).limit(limit).all()

def create_text(db: Session, text: TextCreate):
    db_text = Text_model(**text.dict())
    db.add(db_text)
    db.commit()
    db.refresh(db_text)
    return db_text