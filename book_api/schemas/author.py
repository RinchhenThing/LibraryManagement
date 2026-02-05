from pydantic import BaseModel
from typing import Optional 

class AuthorCreate(BaseModel):
    name: str 

class AuthorResponse(AuthorCreate):
    id: int 
    
    class Config:
        from_attributes = True 


class AuthorUpdate(BaseModel):
    name: Optional[str] = None #here opional means the data can stay unchanged as well.
