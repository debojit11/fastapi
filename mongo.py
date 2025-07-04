from pymongo import MongoClient
from fastapi import FastAPI, status
from pydantic import BaseModel
from typing import List

client= MongoClient()

class Book(BaseModel):
   bookID: int
   title: str
   author:str
   publisher: str

app= FastAPI()

DB = "mydb"
BOOK_COLLECTION = "books"

@app.post('/add_new', status_code=status.HTTP_201_CREATED)
async def add_book(b1:Book):
   """Post a new message to the specified channel."""
   with MongoClient("mongodb://admin:admin@127.0.0.1:27017/") as client:
      book_collection= client[DB][BOOK_COLLECTION]
      result = book_collection.insert_one(b1.dict())
      ack = result.acknowledged
      return{'insertion':ack}
   

@app.get('/books', response_model=List[str])
async def get_books():
   """Get all books in list form."""
   with MongoClient("mongodb://admin:admin@127.0.0.1:27017/") as client:
      book_collection= client[DB][BOOK_COLLECTION]
      booklist = book_collection.distinct('title')
      return booklist
   

@app.get('/books/{id}', response_model=Book)
async def get_book(id: int):
    """Get all messages for the specified channel."""
    with MongoClient("mongodb://admin:admin@127.0.0.1:27017/") as client:
       book_collection= client[DB][BOOK_COLLECTION]
       b1 = book_collection.find_one({'bookID':id})
       return b1