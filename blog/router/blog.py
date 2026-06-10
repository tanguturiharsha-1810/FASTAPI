from fastapi import FastAPI,Depends,status,Response,HTTPException,APIRouter
import schemas,database,Models
from typing import Any
from sqlalchemy.orm import Session
from repository import blog
import oauth2

router =APIRouter (
   prefix='/blog',
   tags=['Blogs']
)
   

get_db= database.get_db

@router.get('/',response_model=list[schemas.ShowBlog])
def get_blogs(db:Session=Depends(get_db),current_user:schemas.User = Depends(oauth2.get_current_user)):
   return blog.get_all(db)

@router.get('/{id}',status_code=200,response_model=schemas.ShowBlog)
def get_blog_byId(id:int,response:Response,db:Session=Depends(get_db),current_user:schemas.User = Depends(oauth2.get_current_user)):
   return blog.get_byId(id,db)
   

@router.post('/',status_code=status.HTTP_201_CREATED)
def create_blog(request:schemas.Blog,db:Session=Depends(get_db),current_user:schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request,db)

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update_blog(id:int,request:schemas.Blog,db:Session=Depends(get_db),current_user:schemas.User = Depends(oauth2.get_current_user)):
   return blog.update(id,request,db)


@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id:int,db:Session=Depends(get_db),current_user:schemas.User = Depends(oauth2.get_current_user)):
   return blog.delete_blog(id,db)
 