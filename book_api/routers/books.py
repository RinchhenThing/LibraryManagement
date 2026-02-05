from fastapi import APIRouter, Depends, HTTPException 
from sqlalchemy.orm import Session 
from database import SessionLocal
from models.book import Book 
from schemas.book import BookCreate, BookResponse, BookUpdate

#unq: routers/books

router = APIRouter(
    prefix="/books",
    tags=["books"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close() 

@router.post("/", response_model=BookResponse) 
#here we'll use a dependency injection for DB connection 
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    db_book = Book(
        title=book.title,
        author_id=book.author_id,
        is_rented=book.is_rented
    )
    db.add(db_book) 
    db.commit()
    db.refresh(db_book) 
    return db_book 

#to list the books 
@router.get("/", response_model=list[BookResponse])
def list_books(db: Session = Depends(get_db)):
    return db.query(Book).all()

#to get by id 
@router.get("/{book_id}", response_model=BookResponse)
def get_book(book_id: int, db:Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status=404, details="Book not found")
    return book 

#to update the books field 
@router.put("/{book_id}", response_model=BookResponse)
def update_book(
        book_id: int,
        book_update: BookUpdate,
        db: Session = Depends(get_db)
):
    #first fetcht the records
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status=400, details="Book not found")

    #not lets update what is to from the input 
    if book_update.title is not None:
        book.title = book_update.title
    if book_update.author_id is not None:
        bool.author_id = book_update.author_id
    if book_update.is_rented is not None:
        book.is_rented = book_update.is_rented

    db.commit()
    db.refresh(book)
    return book 

#and now to delete 
@router.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status=400, details="Book not found")

    db.delete(book)
    db.commit()
    return {"message": "Book Deleted"}
