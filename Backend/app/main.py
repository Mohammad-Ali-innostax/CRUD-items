from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from . import database, schemas
from typing import List
import bcrypt

app = FastAPI()

#adding cors middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_hashed_password(plain_password):
    return bcrypt.hashpw(plain_password.encode('utf-8'), bcrypt.gensalt())
def check_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password)

# @app.get("/", response_model=List[schemas.User])
# def read_users(db:Session = Depends(database.get_db)):
#     return db.query(database.User)

@app.post("/login/")
def read_user(userData: List[schemas.UserCreate], db:Session = Depends(database.get_db)):
    receivedUsername = userData[0].username
    receivedPassword = userData[0].password
    #getting the database user details based on the username
    db_user = db.query(database.User).filter(database.User.username == receivedUsername).first()
    if db_user == None or not check_password(receivedPassword, db_user.password):
        return False
    return True


@app.post("/register/")
def create_user(userData: List[schemas.UserCreate], db:Session = Depends(database.get_db)):
    new_user = database.User(username= userData[0].username, password= userData[0].password)
    new_user.password = get_hashed_password(new_user.password) #hashing the password with salt
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return "200"

@app.exception_handler(HTTPException) #formatting the error response
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code= exc.status_code,
        content= [{"detail": exc.detail}]
        ) 
