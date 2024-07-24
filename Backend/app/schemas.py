from pydantic import BaseModel

class UserBase(BaseModel):
    username:str
    password:str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id:int
    
    class config():
        orm_mode = True