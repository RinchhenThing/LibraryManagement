from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session 
from database import SessionLocal
from models.author import Author
from schemas.author import AuthorCreate, AuthorResponse, AuthorUpdate

#unq : routers/authors 

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

#to list the authors
@router.get("/", response_model=list[AuthorResponse])
def list_authors(db: Session = Depends(get_db)):
    return db.query(Author).all()

#to get by id 
@router.get("/{author_id}", response_model=AuthorResponse)
def get_author(author_id:int, db:Session = Depends(get_db)):
    author = db.query(Author).filter(Author.id  == author_id).first()
    if not author:
        raise HTTPException(status_code=404, details="Author not found")
    return author 

#now to update the data
@router.put("/{author_id}", response_model=AuthorResponse)
def update_author(
        author_id: int,
        author_update: AuthorUpdate,
        db: Session = Depends(get_db)
):
    #first fetch the record 
    author = db.query(Author).filter(Author.id == author_id).first()
    if not author:
        raise HTTPException(status_code=404, details="Author not found")
    
    #then update the record 
    if author_update.name is not None: 
        author.name = author_update.name 

    db.commit()
    db.refresh(author)
    return author 

#and now to delete 
@router.delete("/{author_id}")
def delete_book(author_id: int, db: Session = Depends(get_db)):
    author = db.query(Author).filter(Author.id == author_id).first()
    if not author:
        raise HTTPException(status_code=404, details="Author not found")
    db.delete(Author)
    db.commit()
    return {"message": "Author deleted"}







         
