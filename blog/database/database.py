import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base



db_url= os.getenv("DATABASE_URL")

engine= create_engine(db_url,)

sessionLocal = sessionmaker(autoflush=False,autocommit=False,bind=engine)

Base = declarative_base()

def get_db():
    db = sessionLocal()
    try:
      yield db
    finally:
      db.close()