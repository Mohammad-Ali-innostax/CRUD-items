from sqlalchemy import create_engine,String, Integer, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///models.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(engine)
Base = declarative_base()


class Item(Base):
    __tablename__ = "items"
    
    id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String, index=True)
    brand_name = Column(String, index=True)
    price = Column(Integer, index=True)
    
Base.metadata.create_all(bind = engine)



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
