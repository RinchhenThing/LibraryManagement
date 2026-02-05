from fastapi import APIRouter, Depends 
from sqlalchemy.orm import Session 
from database import SessionLocal
from models.author import Author
from schemas.author import AuthorCreate, AuthorResponse 

router = APIRouter(
    prefix="/authors",
    tags=["authors"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close() 

@router.post("/", response_model=AuthorResponse)
#here we'll use a dependency injection for DB connection 
def create_author(author: AuthorCreate, db: Session = Depends(get_db)):
    db_author = Author(name=author.name) 
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author 

