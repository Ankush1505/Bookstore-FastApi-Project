from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List, Optional
import models, schemas, database 



router = APIRouter(
    prefix="/books",      
    tags=["Books"]  
)

# Get all Book Section
@router.get("/", response_model=List[schemas.Book_with_votes])
def get_books(db: Session = Depends(database.get_db), author: Optional[str] = None): # Added optional author query parameter
    # Store the query first, joining the Book and Vote models and grouping them by book id
    query = (
        # Select the Book model and a count of votes labeled as "Votes"
        db.query(models.Book, func.count(models.Vote.book_id).label("votes"))
        # Perform an outer join on the Vote model using the book id
        .join(models.Vote, models.Vote.book_id == models.Book.id, isouter=True)
        # Group the results by the book id to ensure accurate vote counts
        .group_by(models.Book.id)
    )
    
    # Check if the optional author parameter is provided (not None)
    if author:
        # Conditionally add a filter to the query using .contains() for partial matches
        query = query.filter(models.Book.author.contains(author))
        
    # Execute the fully constructed query using .all() at the very end
    result = query.all()
    
    # Return the list of matching books with their vote counts
    return result

# Create a Book
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(database.get_db)):
    new_book = models.Book(**book.dict())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

# Get Book By Id
@router.get("/{id}", response_model=schemas.Book_with_votes)
def get_book(id: int, db: Session = Depends(database.get_db)):
    book = (db.query(models.Book, func.count(models.Vote.book_id).label("votes"))
             .join(models.Vote, models.Vote.book_id == models.Book.id, isouter=True)
             .group_by(models.Book.id)
            .filter(models.Book.id == id).first())
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with id: {id} not found")
    return book

# Delete Book by Id
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(id: int, db: Session = Depends(database.get_db)):
    book_query = db.query(models.Book).filter(models.Book.id == id)

    if book_query.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with Id: {id} doesn't exist.")
    
    book_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# Update the book by id
@router.put("/{id}", response_model=schemas.Book)
def update_book(id: int, updated_book: schemas.BookCreate, db: Session = Depends(database.get_db)):
    book_query = db.query(models.Book).filter(models.Book.id == id)
    book = book_query.first()

    if book == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with id: {id} does not exist")

    book_query.update(updated_book.dict(), synchronize_session=False)
    db.commit()
    return book_query.first()
