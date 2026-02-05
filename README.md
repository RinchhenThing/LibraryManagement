# Project: Library Book Manager 

## What am I building?

--- 

## Entities (table)
We'll start with two tables
  **a. Author**
  **b. Book**

## Relationship
  - One **Author** -> many **books**
  - Each Book belongs to one Author

  So:
  **Aurthor -> Books** = one to many
  **Book to Author** = one to one. 

--- 

## Final API features 
  - Create Author
  - List authors
  - Create books (linked to author)
  - List books 
  - See books by author 

--- 

## Tech choices 
- **fastapi** -> APU framework 
- **SQLite** -> zero setup DB 
- **SQLALchemy (ORM)** -> industry standard
- **Pydantic** -> validation

--- 
## Mental Model (Request Flow)

Now lets make a simple mental map 
  To put it into layers:
  
  Request (JSON)
    |
  Schema (Pydantic) -> validation
    |
  Route (FastAPI)
    |
  Model (SQLALchemy) -> database tables 
    |
  Database 

#Project Structure 
book_api/
├── main.py
├── database.py
├── models/
│   ├── __init__.py
│   ├── author.py
│   └── book.py
├── schemas/
│   ├── __init__.py
│   ├── author.py
│   └── book.py
├── routers/
│   ├── __init__.py
│   ├── authors.py
│   └── books.py


First: Lets setup  the database 
a. pip install sqlalchemy
b. write database.py 

Then, lets focus on models
  this is where the PK and FK live  
a. Lets write a model for author then book 

Now, Lets move towards writing the schemas 
a. Author 
b. Book 
