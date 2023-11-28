from sqlalchemy.orm import Session

# from model import User
 
from model import Chat

from schema import ChatSchema

# None / User
# def db_register_user(db: Session, username):
#     db_item = User(username=username)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item

def db_get_chat(db: Session):
    return db.query(Chat).all()

def db_add_chat(db: Session, chat: ChatSchema):
    db_item = Chat(username = chat.username,
                   content= chat.content,
                   timestamp= chat.timestamp)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
