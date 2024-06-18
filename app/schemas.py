from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserResponse(BaseModel):
    username: str
    email: str
    id: str

class UserLogin(BaseModel):
    email: str
    password: str

class LinkID(BaseModel):
    user_id: str
    external_id: str
