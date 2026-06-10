import Models,schemas
from fastapi import FastAPI,Depends,status,Response,HTTPException,APIRouter
from sqlalchemy.orm import Session
from hashing import Hash

def create(request:schemas.User,db:Session=Depends):
   new_user = Models.User(name=request.name,Email=request.Email,password=Hash.bcrypt(request.password))
   db.add(new_user)
   db.commit()
   db.refresh(new_user)
   return new_user

def get_byid(id:int,db:Session=Depends):
   users=db.query(Models.User).filter(Models.User.id==id).first()
   if not users:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'user with the id {id} is not available')
   return users