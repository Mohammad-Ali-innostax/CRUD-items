from pydantic import BaseModel

class ItemBase(BaseModel):
    item_name:str
    brand_name:str
    price:int

class ItemCreate(ItemBase):
    pass

class ItemUpdate(ItemBase):
    pass

class Item(ItemBase):
    id:int
    
    class config():
        orm_mode = True