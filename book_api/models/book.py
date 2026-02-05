from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from database import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    is_rented = Column(Boolean, default=False)

    #authors.id = primary_key, books.author_id = ForeignKey
    author_id = Column(Integer, ForeignKey("authors.id"))
    
