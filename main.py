from fastapi import FastAPI, Path, Query, Body, Request, Form, File, UploadFile, Cookie, Header
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import List, Optional
from pydantic import BaseModel, Field
app = FastAPI()
@app.get('/')
async def root():
    return {'message':'hello world'}

# @app.get('/hello/{name}/{age}')
# async def hello(*, name:str=Path(..., min_length=3, max_length=10), age:int=Path(..., ge=1, le=100), percent:float=Query(..., ge=0, le=100)):
#     return {'name': name, 'age':age}

class Student(BaseModel):
    id:int
    name:str=Field(None, description='name of student', max_length=10)
    subjects:List[str]=[]

@app.post('/students/{college}')
async def student_data(college:str, age:int, student:Student):
    retval = {"college":college, "age": age, **student.dict()}
    return retval

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


@app.get('/login/', response_class=HTMLResponse)
async def login(request:Request):
    return templates.TemplateResponse('login.html', {'request':request})


@app.post('/submit/')
async def submit(nm:str=Form(...), pwd:str=Form(...)):
    return {'username': nm}

import shutil
@app.get('/upload/', response_class=HTMLResponse)
async def upload(request:Request):
    return templates.TemplateResponse('uploadfile.html', {'request':request})


@app.post('/uploader/')
async def create_upload_file(file:UploadFile = File(...)):
    with open('destination.png', 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {'filename':file.filename}


@app.post('/cookie/')
async def create_cookie():
    content = {'message': "cookie set"}
    response = JSONResponse(content=content)
    response.set_cookie(key='username', value='admin')
    return response


@app.get('/readcookie/')
async def read_cookie(username:str = Cookie(None)):
    return {'username': username}


@app.get('/headers/')
async def read_header(accept_language: Optional[str] = Header(None)):
    return {'Accept-language': accept_language}


@app.get('/rspheader/')
def set_rsp_headers():
    content = {'message': 'Hello World'}
    headers = {'X-Web-Framework': 'FastAPI', 'Content-Language': 'en-US'}
    return JSONResponse(content=content, headers=headers)