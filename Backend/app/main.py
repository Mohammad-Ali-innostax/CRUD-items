from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from . import database, schemas
from typing import List

app = FastAPI()

#adding cors middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_model=List[schemas.User])
def read_users(db:Session = Depends(database.get_db)):
    return db.query(database.User)

@app.post("/login/")
def read_user(userData: List[schemas.UserCreate], db:Session = Depends(database.get_db)):
    db_user = db.query(database.User).filter(database.User.username == userData[0].username, database.User.password == userData[0].password).first()
    if db_user == None:
        return False
    return True


@app.post("/register/")
def create_user(userData: List[schemas.UserCreate], db:Session = Depends(database.get_db)):
    print(userData[0].username)
    new_user = database.User(username= userData[0].username, password= userData[0].password)
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
