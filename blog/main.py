
from fastapi import FastAPI
from database import engine
import Models
from router import blog,user,authentication


app= FastAPI()

Models.Base.metadata.create_all(bind=engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)



