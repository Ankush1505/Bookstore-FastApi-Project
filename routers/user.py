from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
import models, schemas, database
import utils  # <--- importing the hashing tool

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

# --- CREATE USER (SIGN UP) ---
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    
    # 1. Hash the password (turn "password123" into secret code)
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    
    # 2. Create the user model
    new_user = models.User(**user.dict())
    
    # 3. Add to Database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user

# --- GET USER (Optional, for testing) ---
@router.get("/{id}", response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id: {id} does not exist")
        
    return user