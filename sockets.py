from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

templates= Jinja2Templates(directory='templates')

app= FastAPI()
app.mount('/static', StaticFiles(directory='static'), name='static')
@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse('socket.html', {'request':request})


from fastapi import WebSocket
@app.websocket('/ws')
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was {data}")