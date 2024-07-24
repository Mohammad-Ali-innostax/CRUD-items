from sqlalchemy import create_engine,String,Integer, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///userAuthentication.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(engine)
Base = declarative_base()


class User(Base):
    __tablename__ = "AuthenticationTable"
    
    id = Column(Integer, primary_key=True, index=True)
    Username = Column(String, index=True)
    password = Column(String, index=True)
    
Base.metadata.create_all(bind = engine)



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
