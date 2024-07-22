from pydantic import BaseModel

class ItemBase(BaseModel):
    name:str
    age:int

class ItemCreate(ItemBase):
    pass

class ItemUpdate(ItemBase):
    pass

class Item(ItemBase):
    id:int
    
    class config():
        orm_mode = True