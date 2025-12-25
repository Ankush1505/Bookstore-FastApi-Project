from fastapi import FastAPI
import models
from database import engine
from routers import books, user, auth, votes 
from fastapi.middleware.cors import CORSMiddleware

# Created Database Table 
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_methods = ["*"],
    allow_headers = ["*"],
    allow_credentials = True,
)



# Connect the Router to the Main.
app.include_router(books.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(votes.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Bookstore API"}