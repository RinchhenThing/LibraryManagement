from fastapi import APIRouter, Depends 
from sqlalchemy.orm import Session 
from database import SessionLocal
from models.book import Book 
from schemas.book import BookCreate, BookResponse 

router = APIRouter(
    prefix="/books",
    tags=["books"]
)

def get_db():
    db = SessionLocal()
    try:
        yeild db 
    finally:
        db.close() 

@router.post("/", response_model=BookResponse) 
#here we'll use a dependency injection for DB connection 
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    db_book = Book(
        title=book.title,
        author_id=book.author_id 
    )
    db.add(db_book) 
    db.commit()
    db.refresh(db_book) 
    return db_book 

