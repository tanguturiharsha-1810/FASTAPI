from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import blog.auth.tokens as tokens
from sqlalchemy.orm import Session
import blog.database.database as database
import blog.models.models as Models

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

def get_current_user(token: str = Depends(oauth2_scheme),db: Session = Depends(database.get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    token_data = tokens.verify_token(token, credentials_exception)
    user = db.query(Models.User).filter(Models.User.Email == token_data.Email).first()
    if user is None:
        raise credentials_exception
    return user
    

   