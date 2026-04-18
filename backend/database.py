from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from backend.config import setting

DATABASE_URL = setting.db_url

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def connect_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
