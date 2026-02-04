#Project: Library Book Manager 

#What am I building?

Entities (table)
= We'll start with two tables
  a. Author
  b. Book

Relationship
  - One Author -> many books
  - Each Book belongs to one Author

  So, Aurthor -> Books is one to many
      and Book to Author is one to one. 

#Final API features 
  a. Create Author
  b. List authors
  c. Create books (linked to author)
  d. List books 
  e. See books by author 

#Tech choices 
  a. fastapi -> APU framework 
  b. SQLite -> zero setup DB 
  c. SQLALchemy (ORM) -> industry standard
  d. Pydantic -> validation


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



