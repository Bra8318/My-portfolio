from sqlalchemy import Column, String,Integer,Text, DateTime
from database import Base
from datetime import datetime

class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String,index=True)
    email = Column(String,index=True)
    message = Column(Text)
    timestamp = Column(DateTime, default=datetime.now)

class data(Base):
    __tablename__ = "upload_file"
    id = Column(Integer, primary_key=True, index=True)
    photo = Column(String,index=True)
    cv = Column(String,index=True)

