import blog.models.models as Models,blog.schemas.schemas as schemas
from fastapi import FastAPI,Depends,status,Response,HTTPException,APIRouter
from sqlalchemy.orm import Session



def get_all(db:Session):
    blogs=db.query(Models.Blog).all()
    return blogs

def get_byId(id:int,db:Session):
   blogs=db.query(Models.Blog).filter(Models.Blog.id==id).first()
   if not blogs:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with the id {id} is not available')
   return blogs

def create(request:schemas.Blog,db:Session,current_user:schemas.User):
    new_blog = Models.Blog(title=request.title,body=request.body,current_user_id=current_user.id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog 


def update(id:int,request:schemas.Blog,db:Session=Depends):
   blog=db.query(Models.Blog).filter(Models.Blog.id==id)
   if not blog.first():
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with the id {id} is not available')
   blog.update({'title':request.title,'body':request.body})
   db.commit()
   return 'blog updated successfully'

def delete_blog(id:int,db:Session=Depends):
   blog=db.query(Models.Blog).filter(Models.Blog.id==id)
   if not blog.first():
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with the id {id} is not available')
   blog
   blog.delete(synchronize_session=False)
   db.commit()
   return 'Blog deleted successfully'