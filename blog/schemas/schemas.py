from pydantic import BaseModel
from typing import Any
from pydantic import ConfigDict


class Blog(BaseModel):
    title:str
    body:str
    class Config(ConfigDict):
        model_config = ConfigDict(from_attributes=True)

class User(BaseModel):
    name:str
    Email:str
    password:str

class ShowUser(BaseModel):
    name:str
    Email:str
    blogs:list[Blog]
    class Config(ConfigDict):
        model_config = ConfigDict(from_attributes=True)

class ShowBlog(BaseModel):
    title:str
    body:str
    creator:ShowUser
    class Config(ConfigDict):
        model_config = ConfigDict(from_attributes=True)

class Login(BaseModel):
    username:str
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    Email: str | None = None