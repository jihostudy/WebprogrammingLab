from typing import List
from fastapi import FastAPI, Request, Response, Depends, WebSocket

from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from sqlalchemy.orm import Session
# db관련 import
from model import Base, Chat
from crud import db_get_chat, db_add_chat
from database import SessionLocal, engine
from schema import ChatSchema, ChatSchemaAdd

app = FastAPI()

# css, js 추가시키기
app.mount("/static", StaticFiles(directory="static"), name="static")
# template
templates = Jinja2Templates(directory="templates")

# db
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# WebSocket
class ConnectionManager:
    def __init__(self):
        self.active_connections = []
    # 연결시키기
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
    # 해제시키기
    async def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)
    # 뿌리기
    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

            
# 관리 객체 만들기
socket_manager = ConnectionManager()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await socket_manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await socket_manager.broadcast(f"{data}")
    except Exception as e:
        pass
    finally:
        await socket_manager.disconnect(websocket)

# 초기 실행
@app.get("/")
def get_root(req: Request):    
    return templates.TemplateResponse("index.html",{"request":req})
    
# chat 입력시
@app.post("/chat", response_model=List[ChatSchema])
def add_chat(chat: ChatSchemaAdd,
             db: Session = Depends(get_db)):
    result = db_add_chat(db, chat)
    if not result:
        print("not result")
        return None
    print("Yes result")
    return db_get_chat(db)


# username입력하고 채팅가져오기 버튼을 클릭했을때
@app.get("/chat")
def get_chat(db: Session = Depends(get_db)):
    result = db_get_chat(db)
    if result:
        return result
    else:
        return None



# username 입력시 이에 해당하는 Chat불러오기 (쿠키가 없을 떄에만 실행된다)
# User 생성하기 + Chat 불러오기
# @app.post("/register")
# def register_user(response: Response,
#                   data: OAuth2PasswordRequestForm = Depends(),
#                   db: Session = Depends(get_db)):
#     username = data.username    
#     user = db_register_user(db, username)
#     if user:
#         access_token =  manager.create_access_token(
#             data = {'sub': username}
#         )
#         manager.set_cookie(response, access_token)
#         return db_get_chat(db)
#     else :        
#         return db_get_chat(db) 




