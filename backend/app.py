from fastapi import Depends, FastAPI, Request, Form, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import model
from database import connect_db, Base, engine, SessionLocal
from typing import Annotated, Optional
from schema import ContactForm
import schema
import os
import shutil
import uuid
import cloudinary
import cloudinary.uploader
from config import setting


app = FastAPI()

origins = ["http://127.0.0.1:5500","https://brajesh-kumar.vercel.app"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

cloudinary.config(
    cloud_name = setting.cloud_name,
    api_key = setting.api_key,
    api_secret = setting.api_secret
)
# UPLOAD_DIR = "uploads"
# os.makedirs(UPLOAD_DIR, exist_ok=True)

# # Serve uploaded files
# app.mount("/uploads", StaticFiles(directory=UPLOAD_DIR), name="uploads")

model.Base.metadata.create_all(bind=engine)

db_dependency = Annotated[SessionLocal, Depends(connect_db)]

@app.get('/')
def home():
    return {"message": "Welcome to Brajesh Kumar's Portfolio!"}

@app.post('/contact')
def contact(contact: schema.ContactForm, db: db_dependency): # type: ignore
    new_contact = model.Contact(
        name=contact.name,
        email=contact.email,
        message=contact.message
    )
    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)
    return {"status": "success", "message": "Thank you for contacting me!"}

@app.get('/show_contacts')
def show_contacts(db: db_dependency): # type: ignore
    contacts = db.query(model.Contact).all()
    return contacts

@app.post('/delete_contacts/{id}')
def delete_contacts(id: int, db: db_dependency): # type: ignore
    contact = db.query(model.Contact).filter(model.Contact.id == id).first()
    if contact is None:
        return {"status": "error", "message": "Contact not found"}
    db.delete(contact)
    db.commit()
    return {"status": "success", "message": "Contact deleted Successfully"}

@app.post('/upload_photo')
def upload_photo(db: db_dependency, photo: UploadFile = File(...)): # type: ignore
    if not photo.content_type.startswith('image/'):
        return {"status": "error", "message": "Only image files are allowed"}
    
    try:
        result = cloudinary.uploader.upload(ptoto.file,
        folder = "portfolio/photos")
       
        image_url = result["secure_url"]
        record = db.query(model.data).first()
        if record is None:
            record = model.data(photo=image_url, cv=None)
            db.add(record)
        else:
            record.photo = image_url
    
        db.commit()
        db.refresh(record)
    
        return {
            "status": "success",
            "message": "Photo uploaded successfully",
            "photo": image_url
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.post('/upload_cv')
def upload_cv(db: db_dependency, cv: UploadFile = File(...)): # type: ignore
    valid_types = ['application/pdf', 'application/msword', 
                   'application/vnd.openxmlformats-officedocument.wordprocessingml.document']
    
    if cv.content_type not in valid_types:
        return {"status": "error", "message": "Only PDF, DOC, DOCX files are allowed"}
    
    try:
        result = cloudinary.uploader.upload(cv.file,
        resource_type = "raw",
        folder = "portfolio/cv")

        file_url = result["secure_url"]
    
    
        record = db.query(model.data).first()
        if record is None:
            record = model.data(photo=None, cv=file_url)
            db.add(record)
        else:
            record.cv = file_url
    
        db.commit()
        db.refresh(record)
    
        return {
            "status": "success",
            "message": "CV uploaded successfully",
            "cv": file_url
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}
@app.get('/get_files')
def get_files(db: db_dependency): # type: ignore
    record = db.query(model.data).first()
    if record is None:
        return {"photo": None, "cv": None}
    return {"photo": record.photo, "cv": record.cv}
