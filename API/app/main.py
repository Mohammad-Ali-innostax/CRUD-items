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

@app.get("/items/", response_model=List[schemas.Item])
def read_items(db:Session = Depends(database.get_db)):
    return db.query(database.Item)

@app.get("/items/{item_id}", response_model=List[schemas.Item])
def read_item(item_id:int, db:Session = Depends(database.get_db)):
    db_item = db.query(database.Item).filter(database.Item.id == item_id).first()
    if db_item == None:
        raise HTTPException(status_code=404, detail="Item not found")
    return [db_item]

@app.post("/items/", response_model=List[schemas.Item] )
def create_item(items: List[schemas.ItemCreate], db:Session = Depends(database.get_db)):
    db_items = []
    for item in items:
        new_item = database.Item(item_name= item.item_name, brand_name= item.brand_name, price = item.price)
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
        db_items.append(new_item)
    return db_items

@app.put("/items/{item_id}", response_model=List[schemas.Item])
def update_item(item_id:int, item: List[schemas.ItemUpdate], db:Session = Depends(database.get_db)):
    old_item = read_item(item_id, db)[0]  #getting the first item
    if old_item == None:
        raise HTTPException(status_code=404, detail="Item not found")
    old_item.item_name = item[0].item_name 
    old_item.brand_name = item[0].brand_name
    old_item.price = item[0].price
    
    db.commit()
    db.refresh(old_item)
    return [old_item]

@app.delete("/items/{item_id}", response_model=List[schemas.Item])
def delete_user(item_id:int, db:Session = Depends(database.get_db)):
    db_item = read_item(item_id, db)[0]
    if db_item == None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return [db_item]

@app.exception_handler(HTTPException) #formatting the error response
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code= exc.status_code,
        content= [{"detail": exc.detail}]
        ) 