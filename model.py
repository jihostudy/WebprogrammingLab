from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from database import Base

# 파이널 과제를 위한 미리 짜기

# 유저
# class User(Base):
#     __tablename__ = "User"

#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String, index=True)
    # email = Column(String)
    # password = Column(String)    

# 채팅 모델
class Chat(Base):
    __tablename__ = "Chat"

    id = Column(Integer, primary_key=True, index=True)    
    content = Column(String)
    timestamp = Column(DateTime)
    username = Column(String)
    # user_id = Column(Integer, ForeignKey("User.id"))
    # user = relationship("User")
    # chatroom_id = Column(Integer, ForeignKey("ChatRoom.id"))

# 채팅방
# class ChatRoom(Base):
#     __tablename__ = "ChatRoom"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)

# # 채팅방 멤버 필드
# class ChatRoomMember(Base):
#     __tablename__ = "ChatRoomMember"
#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey("User.id"))
#     chatroom_id = Column(Integer, ForeignKey("ChatRoom.id"))

# # 채팅 모델
# class Chat(Base):
#     __tablename__ = "Chat"
#     id = Column(Integer, primary_key=True, index=True)
#     content = Column(String)
#     user_id = Column(Integer, ForeignKey("User.id"))
#     chatroom_id = Column(Integer, ForeignKey("ChatRoom.id"))
#     timestamp = Column(DateTime, default=datetime.utcnow)
