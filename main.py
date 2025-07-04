from fastapi import FastAPI, Path, Query, Body, Request, Form, File, UploadFile, Cookie, Header, Depends, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import List, Optional, Tuple
from pydantic import BaseModel, Field

app = FastAPI()

# origins = ['https://127.0.0.1', 'http://127.0.0.1', 'https://127.0.0.1:8000', 'https://ominous-system-j6xgq9vq65vhqg6r-8000.app.github.dev']

# app.add_middleware(CORSMiddleware, allow_origins= origins, allow_credentials=True, allow_methods=['*'], allow_headers=['*'])

@app.get('/')
async def root():
    return {'message':'hello world'}


# @app.get('/hello/{name}/{age}')
# async def hello(*, name:str=Path(..., min_length=3, max_length=10), age:int=Path(..., ge=1, le=100), percent:float=Query(..., ge=0, le=100)):
#     return {'name': name, 'age':age}

# class Student(BaseModel):
#     id:int
#     name:str=Field(None, description='name of student', max_length=10)
#     subjects:List[str]=[]


# @app.post('/students/{college}')
# async def student_data(college:str, age:int, student:Student):
#     retval = {"college":college, "age": age, **student.dict()}
#     return retval


# @app.get('/hello/')
# async def hello():
#     ret='''
# <html>
# <body>
# <h2>Hello World</h2>
# <body>
# <html>
# '''
#     return HTMLResponse(content=ret)


templates = Jinja2Templates(directory='templates')
# app.mount("/static", StaticFiles(directory='static'), name='static')
# @app.get('/hello/{name}', response_class=HTMLResponse)
# async def hello(request:Request, name:str):
#     return templates.TemplateResponse("hello.html", {'request':request, "name":name})


# @app.get('/login/', response_class=HTMLResponse)
# async def login(request:Request):
#     return templates.TemplateResponse('login.html', {'request':request})


# @app.post('/submit/')
# async def submit(nm:str=Form(...), pwd:str=Form(...)):
#     return {'username': nm}

# import shutil
# @app.get('/upload/', response_class=HTMLResponse)
# async def upload(request:Request):
#     return templates.TemplateResponse('uploadfile.html', {'request':request})


# @app.post('/uploader/')
# async def create_upload_file(file:UploadFile = File(...)):
#     with open('destination.png', 'wb') as buffer:
#         shutil.copyfileobj(file.file, buffer)
#     return {'filename':file.filename}


# @app.post('/cookie/')
# async def create_cookie():
#     content = {'message': "cookie set"}
#     response = JSONResponse(content=content)
#     response.set_cookie(key='username', value='admin')
#     return response


# @app.get('/readcookie/')
# async def read_cookie(username:str = Cookie(None)):
#     return {'username': username}


# @app.get('/headers/')
# async def read_header(accept_language: Optional[str] = Header(None)):
#     return {'Accept-language': accept_language}


# @app.get('/rspheader/')
# def set_rsp_headers():
#     content = {'message': 'Hello World'}
#     headers = {'X-Web-Framework': 'FastAPI', 'Content-Language': 'en-US'}
#     return JSONResponse(content=content, headers=headers)


# class Student(BaseModel):
#     id:int
#     name: str = Field(None, description='name of student', max_length=10)
#     marks: List[int]=[]
#     percent_marks: float

# class Percent(BaseModel):
#     id: int
#     name: str = Field(None, description='name of student', max_length=10)
#     percent_marks: float

# @app.post('/marks', response_model=Percent)
# async def get_percent(s1:Student):
#     s1.percent_marks = sum(s1.marks)/2
#     return s1


# class supplier(BaseModel):
#     supplierID: int
#     supplierName: str

# class product(BaseModel):
#     productID: int
#     prodname: str
#     price: int
#     supp: supplier

# class customer(BaseModel):
#     custID: int
#     custName: str
#     prod: Tuple[product]

# @app.post('/invoice')
# async def getInvoice(c1:customer):
#     return c1


# class dependency:
#     def __init__(self, id:str, name:str, age:int):
#         self.id = id
#         self.name = name
#         self.age = age

# @app.get('/users/')
# async def users(dep: dependency = Depends(dependency)):
#     return dep

# @app.get('/admin/')
# async def admini(dep: dependency = Depends(dependency)):
#     return dep


# async def validate(dep: dependency = Depends(dependency)):
#     if dep.age > 18:
#         raise HTTPException(status_code=400, detail='you arent eligible')
    
# @app.get('/users/', dependencies=[Depends(validate)])
# async def users():
#     return {'message': 'You are eligible'}


data =[]

class Book(BaseModel):
    id:int
    title: str
    author: str
    publisher: str

# CREATE - POST
@app.post('/book')
async def add_book(book: Book):
    data.append(book.dict())
    return data

# READ-GET
@app.get('/list')
async def get_books():
    return data

@app.get('/book/{id}')
async def get_book(id: int):
    id = id-1
    return data[id]

# UPDATE - PUT
@app.put('/book/{id}')
async def add_book(id:int, book:Book):
    data[id-1]= book
    return data


# DELETE - DELETE
@app.delete('/book/{id}')
async def delete_book(id: int):
    data.pop(id-1)
    return data