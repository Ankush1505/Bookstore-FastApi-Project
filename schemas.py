from pydantic import BaseModel, Field, EmailStr
from datetime import datetime
from typing import Optional

# Base Schema: Shared properties
class BookBase(BaseModel):
    title: str = Field(..., min_length=5, description="Title of the book")
    content: str = Field(..., min_length=5, description="Description of the book")
    published: bool = True
    price: float = Field(default=0.0, ge=0, description="Price in dollars")
    # Validation: Inventory cannot be negative
    inventory: int = Field(default=0, ge=0, description="Stock count")

# Create Schema: Used for POST requests
class BookCreate(BookBase):
    pass 

# 3. Response Schema: Used for GET/PUT responses
class Book(BookBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str

 # User Out (The Receipt we send back)
class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True

class Vote(BaseModel):
    book_id : int
    dir : int = Field(ge=0, le=1)

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

class Book_with_votes(BaseModel):
    Book : Book
    votes : int

    class Config:
        orm_mode = True
