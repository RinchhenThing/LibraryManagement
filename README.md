# Project: Library Book Manager

## What am I building?

A simple **Library Book Manager API** using FastAPI that manages authors and their books.

---

## Entities (Database Tables)

We will start with **two tables**:

- **Author**
- **Book**

### Relationship

- One **Author** ➜ many **Books**
- Each **Book** belongs to **one Author**

So:
- **Author → Books** = one-to-many  
- **Book → Author** = many-to-one  

---

## Final API Features

- Create Author
- List Authors
- Create Books (linked to an Author)
- List Books
- View Books by Author

---

## Tech Choices

- **FastAPI** → API framework
- **SQLite** → Zero-setup database
- **SQLAlchemy (ORM)** → Industry standard ORM
- **Pydantic** → Data validation

---

## Mental Model (Request Flow)

```

Request (JSON)
↓
Schema (Pydantic) → Validation
↓
Route (FastAPI)
↓
Model (SQLAlchemy) → Database Tables
↓
Database

```

---

## Project Structure

```

book_api/
├── main.py
├── database.py
├── models/
│   ├── **init**.py
│   ├── author.py
│   └── book.py
├── schemas/
│   ├── **init**.py
│   ├── author.py
│   └── book.py
├── routers/
│   ├── **init**.py
│   ├── authors.py
│   └── books.py

````

---

## Step 1: Setup the Database

1. Install dependencies:
   ```bash
   pip install sqlalchemy
````

2. Create `database.py`

---

## Step 2: Define Models

This is where **primary keys (PK)** and **foreign keys (FK)** live.

* Create `Author` model
* Create `Book` model

---

## Step 3: Create Schemas (Pydantic)

Schemas handle **input validation and response formatting**.

* Author schema
* Book schema

## Step 4: Routers (API logic)

Routers handle the **API and logic behind apis**.

* Author router 
* Book Router 

## Step 5: Wire everythin in main.py 

Everything that works here will be reached at and routed through the **main.py** file. 




