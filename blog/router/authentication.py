from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

import blog.schemas.schemas as schemas
import blog.database.database as database
import blog.models.Models as Models
import blog.auth.tokens as tokens

from blog.auth.hashing import Hash

router = APIRouter(
    tags=['Authentication']
)

@router.post('/login')
def login(request:OAuth2PasswordRequestForm=Depends(),db:Session = Depends(database.get_db)):
    user = db.query(Models.User).filter(Models.User.Email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Invalid Username or password')
    if not Hash.verify(request.password,user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Invalid Username or password')
    
    access_token = tokens.create_access_token(data={"sub": user.Email})
    return {"access_token": access_token, "token_type": "bearer"}
   


   