from sqlalchemy import create_engine
from sqlalchemy.dialects.sqlite import *

SQLALCHEMY_DATABASE_URL = 'sqlite:///./test.db'
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args= {'check_same_thread': False})

from sqlalchemy.orm import sessionmaker, Session

SessionLocal = sessionmaker(autocommit =False, autoflush=False, bind=engine)

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from sqlalchemy import Column, Integer, String

class Books(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(50), unique=True)
    author = Column(String(50))
    publisher = Column(String(50))
Base.metadata.create_all(bind=engine)

from typing import List
from pydantic import BaseModel, constr

class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    model_config = {
        "from_attributes": True
    }


from fastapi import FastAPI, Depends
app= FastAPI()
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/add_new', response_model=Book)
def add_book(b1:Book, db:Session = Depends(get_db)):
    bk = Books(id=b1.id, title = b1.title, author= b1.author, publisher=b1.publisher)
    db.add(bk)
    db.commit()
    db.refresh(bk)
    return Books(**b1.dict())


@app.get('/list', response_model=List[Book])
def get_books(db:Session= Depends(get_db)):
    recs= db.query(Books).all()
    return recs

@app.get('/book/{id}', response_model=Book)
def get_book(id:int, db:Session=Depends(get_db)):
    return db.query(Books).filter(Books.id==id).first()


@app.put('/update/{id}', response_model=Book)
def update_book(id:int, book:Book, db:Session=Depends(get_db)):
    b1= db.query(Books).filter(Books.id==id).first()
    b1.id=book.id
    b1.title=book.title
    b1.author=book.author
    b1.publisher=book.publisher
    db.commit()
    return db.query(Books).filter(Books.id==id).first()


@app.delete('/delete/{id}')
def del_book(id:int, db: Session = Depends(get_db)):
    try:
        db.query(Books).filter(Books.id==id).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)
    return {'delete_status':'success'}