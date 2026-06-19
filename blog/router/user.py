from fastapi import FastAPI,Depends,status,Response,HTTPException,APIRouter
import blog.schemas.schemas as schemas,blog.database.database as database,blog.models.models as Models
from typing import Any
from sqlalchemy.orm import Session
from blog.auth.hashing import Hash
from blog.repository import user
import blog.auth.oauth2 as oauth2

router =APIRouter(
   prefix='/user',
   tags=['Users']
)

get_db= database.get_db

@router.post('/',response_model=schemas.ShowUser)
def create_user(request:schemas.User,db:Session=Depends(get_db)):
   return user.create(request,db)
 

@router.get('/{id}',response_model=schemas.ShowUser)
def get_user_byid(id:int,db:Session=Depends(get_db),current_user:schemas.User = Depends(oauth2.get_current_user)):
   return user.get_byid(id,db)