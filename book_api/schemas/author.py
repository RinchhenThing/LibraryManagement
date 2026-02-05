from pydantic import BaseModel

class AuthorCreate(BaseModel):
    name: str 

class AuthorResponse(AuthorCreate):
    id: int 
    
    class Config:
        from_attributes = True 

