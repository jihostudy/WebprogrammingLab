from pydantic import BaseModel
from typing import Optional
from datetime import datetime

#사용자 데이터 정의
# class UserSchema(BaseModel):
#     id: Optional[int]
#     username: str

#     # ORM 모드에서 작동하도록 도와준다
#     class Config:
#         orm_mode = True

class ChatSchema(BaseModel):
    id: Optional[int]
    content: Optional[str]
    timestamp: Optional[datetime]
    username: Optional[str]
    # user_id: Optional[int]
    # user: Optional[UserSchema]

    class Config:
        orm_mode = True

class ChatSchemaAdd(BaseModel):
    content: Optional[str]
    timestamp: Optional[datetime]  
    username: Optional[str]  