from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

# Step 1: Create the FastAPI app
app = FastAPI()


# ✅ Welcome message at root URL
@app.get("/")
def read_root():
    return {"message": "📚 Welcome to the Library API! Visit /docs to try it out."}


# Step 2: Define the Book model
class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int


# Step 3: In-memory storage (list of books)
library: List[Book] = []

# Step 4: CRUD Endpoints

# CREATE - Add a new book
@app.post("/books/", response_model=Book)
def create_book(book: Book):
    for b in library:
        if b.id == book.id:
            raise HTTPException(status_code=400, detail="Book with this ID already exists")
    library.append(book)
    return book

# READ - Get all books
@app.get("/books/", response_model=List[Book])
def get_all_books():
    return library

# READ - Get book by ID
@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    for book in library:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

# UPDATE - Update book by ID
@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, updated_book: Book):
    for index, book in enumerate(library):
        if book.id == book_id:
            library[index] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")

# DELETE - Remove book by ID
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for index, book in enumerate(library):
        if book.id == book_id:
            del library[index]
            return {"message": f"Book with ID {book_id} deleted"}
    raise HTTPException(status_code=404, detail="Book not found")






