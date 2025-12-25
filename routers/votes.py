from fastapi import APIRouter, HTTPException, status, Depends
import models, database, oauth2, schemas
from sqlalchemy.orm import Session


router = APIRouter(
    prefix = "/vote",
    tags=["Vote"] 
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_vote(vote: schemas.Vote, db: Session = Depends(database.get_db), current_user: models.User =  Depends(oauth2.get_current_user)):
    book_query = db.query(models.Book).filter(models.Book.id == vote.book_id).first()
    if not book_query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with id: {vote.book_id} does not exist")



    vote_query = db.query(models.Vote).filter(
         models.Vote.book_id == vote.book_id,
        models.Vote.user_id == current_user.id
    )
    found_vote = vote_query.first()

    if (vote.dir == 1):
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Vote already found with this {vote.book_id} Id")
    
        new_vote = models.Vote(user_id = current_user.id, book_id = vote.book_id)

        db.add(new_vote)
        db.commit()
        return {"Message": "Your Vote is Added Successfully"}
    
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Not found your Vote with this {vote.book_id} Id")
        db.delete(found_vote)
        db.commit()
        return {"Message": "Your Vote has been deleted."}