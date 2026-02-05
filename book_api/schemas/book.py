from pydantic import BaseModel
from typing import Optional 

class BookCreate(BaseModel):
    title: str
    author_id: int 

class BookResponse(BookCreate):
    id: int 
    
    class Config:
        from_attributes = True 


class BookUpdate(BaseModel):
    #here optional means we can update one field without hindering the other. 
    title: Optional[str] = None 
    author_id: Optional[int] = None 

