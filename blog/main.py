
from fastapi import FastAPI
from blog.database.database import engine
import blog.models.models as Models
from blog.router import blog, user, authentication


app= FastAPI()

app= FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI Blog API is Running 🚀"}

Models.Base.metadata.create_all(bind=engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)

Models.Base.metadata.create_all(bind=engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)



