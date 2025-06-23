from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Step 1: DB setup
DATABASE_URL = "sqlite:///./books.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# Step 2: SQLAlchemy Book model
class BookDB(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    year = Column(Integer)

Base.metadata.create_all(bind=engine)

# Step 3: Pydantic model
class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int

    class Config:
        orm_mode = True

# Step 4: FastAPI app
app = FastAPI()

# Step 5: API Endpoints

# CREATE
@app.post("/books/", response_model=Book)
def create_book(book: Book):
    db = SessionLocal()
    db_book = db.query(BookDB).filter(BookDB.id == book.id).first()
    if db_book:
        raise HTTPException(status_code=400, detail="Book already exists")
    new_book = BookDB(**book.dict())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    db.close()
    return new_book

# READ - All
@app.get("/books/", response_model=List[Book])
def read_books():
    db = SessionLocal()
    books = db.query(BookDB).all()
    db.close()
    return books

# READ - One
@app.get("/books/{book_id}", response_model=Book)
def read_book(book_id: int):
    db = SessionLocal()
    book = db.query(BookDB).filter(BookDB.id == book_id).first()
    db.close()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

# UPDATE
@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, updated_book: Book):
    db = SessionLocal()
    book = db.query(BookDB).filter(BookDB.id == book_id).first()
    if book is None:
        db.close()
        raise HTTPException(status_code=404, detail="Book not found")
    book.title = updated_book.title
    book.author = updated_book.author
    book.year = updated_book.year
    db.commit()
    db.refresh(book)
    db.close()
    return book

# DELETE
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    db = SessionLocal()
    book = db.query(BookDB).filter(BookDB.id == book_id).first()
    if book is None:
        db.close()
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    db.close()
    return {"message": f"Book with ID {book_id} deleted"}

#uvicorn Day-27:app --reload

