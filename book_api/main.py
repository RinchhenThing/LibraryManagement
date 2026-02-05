from fastapi import FastAPI
from database import engine, Base
from routers import authors, books 

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(authors.router)
app.include_router(books.router) 

