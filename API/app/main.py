from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import database, schemas

app = FastAPI()

@app.get("/items/", response_model=list[schemas.Item])
def read_items(db:Session = Depends(database.get_db)):
    return db.query(database.Item)

@app.get("/items/{item_id}", response_model=schemas.Item)
def read_item(item_id:int, db:Session = Depends(database.get_db)):
    db_item = db.query(database.Item).filter(database.Item.id == item_id).first()
    if db_item == None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@app.post("/items/", response_model=schemas.Item )
def create_item(item: schemas.ItemCreate, db:Session = Depends(database.get_db)):
    new_item = database.Item(item_name= item.item_name, brand_name= item.brand_name, price = item.price)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

@app.put("/items/{item_id}", response_model=schemas.Item)
def update_item(item_id:int, item: schemas.ItemUpdate, db:Session = Depends(database.get_db)):
    old_item = read_item(item_id, db)
    if old_item == None:
        raise HTTPException(status_code=404, detail="Item not found")
    old_item.item_name = item.item_name
    old_item.brand_name = item.brand_name
    old_item.price = item.price
    
    db.commit()
    db.refresh(old_item)
    return old_item

@app.delete("/items/{item_id}", response_model=schemas.Item)
def delete_user(item_id:int, db:Session = Depends(database.get_db)):
    db_item = read_item(item_id, db)
    if db_item == None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return db_item