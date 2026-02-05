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







         
