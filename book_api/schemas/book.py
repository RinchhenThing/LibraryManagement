from pydantic import BaseModel

class BookCreate(BaseModel):
    title: str
    author_id: int 

class BookResponse(BookCreate):
    id: int 
    
    class Config:
        from_attributes = True 

