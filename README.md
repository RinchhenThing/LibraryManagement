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

## Step 5: Wire everything in main.py 

Everything that works here will be reached at and routed through the **main.py** file. 

--- 

## CRUD (Create Read Update and Delete)

CRDU operations are simply for the normal database operations.

We have already created the create operation.

| Operation  | HTTP            | Example               |
| ---------- | --------------- | --------------------- |
| **C**reate | `POST`          | Add author / book     |
| **R**ead   | `GET`           | List authors, get one |
| **U**pdate | `PUT` / `PATCH` | Edit title            |
| **D**elete | `DELETE`        | Remove book           |


So, **moving forward**

## Step 1: Add Update schemas 
We don't reuse the create schemas for update, because **Updates** are usually partial. 

## Step 2: Read (list + get by id)

Here we will write the code to read data to:
- **List all data**
- **Get data by id**

and the code will be added to the router. 


## Step 3: Update
The update is tricky but simple. We first fetch the record
then modify the provided fields (from input) 
and then, Commit -> refresh -> return. All in database. 

So, the changes will be done on the routers.

## Step 4: And finally delete 
Here, its simple. first we fetch the record we want to delete, i.e.  we will keep the requested record in a variable, then, check if it is recorded, then db.delete()

--- 

## Rental 
Now, we will make the books rent-able. 

## Step 1: Database model
First lets add a small, boolean from sqlalchemy.

Then in the book model, lets add the is_rented variable.

## Step 2: Schemas 

Our API should:
- accept is_rented
- return is_rented

so lets, add, the is_rented variable in the BookCreate, BookResponse and BookUpdate schemas.

## Step 3: Router
Now we allow:
- setting rented status 
- updating it later 

**The changes will be made on the routers.**

## Step 4: query parameters

**Now** we will make this happen, we will filter all the books from query this way, we can filter the books using url and list the rented and not rented ones easily. 

## Step 5: Enforce not to delete rented books
We will simply import status and then apply the rule in a if statement, that rented books can't be deleted.


---

## Rental History 

Lets create a rental History table.

**Relationship:**
- One book -> many rantals 
- One rental -> one book 

## Step 1: Create a rental model 




