from sqlalchemy import Column, Integer, ForeignKey, DateTime 
from sqlalchemy.sql import func 
from database import Base 

class Rental(Base):
    __tablename__ = "rentals"

    id = Column(Integer, primary_key=-True, index=True)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    rented_at = Column(DateTime(timezone=True), server_default=func.now())
    returned_at = Column(DateTime(timezone=True), nullable=True)

