from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base



db_url= "postgresql://postgres:Harsha%4018@localhost:5432/blogdb"

engine= create_engine(db_url,)

sessionLocal = sessionmaker(autoflush=False,autocommit=False,bind=engine)

Base = declarative_base()

def get_db():
    db = sessionLocal()
    try:
      yield db
    finally:
      db.close()