from pydantic import BaseModel
from typing import Optional 

class BookCreate(BaseModel):
    title: str
    author_id: int 
    is_rented: bool = False 

class BookResponse(BookCreate):
    id: int 
    
    class Config:
        from_attributes = True 


class BookUpdate(BaseModel):
    #here optional means we can update one field without hindering the other. 
    title: Optional[str] = None 
    author_id: Optional[int] = None 
    is_rented: Optional[bool] = None 

