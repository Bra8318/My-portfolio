from fastapi import Depends, FastAPI, Request, Form, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from backend import model,schema,database
from database import connect_db, Base, engine, SessionLocal
from typing import Annotated, Optional
from schema import ContactForm
import os
import shutil
import uuid


app = FastAPI()

origins = ["http://127.0.0.1:5500"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Serve uploaded files
app.mount("/uploads", StaticFiles(directory=UPLOAD_DIR), name="uploads")

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
    
    file_ext = os.path.splitext(photo.filename)[1]
    unique_filename = f"photo_{uuid.uuid4().hex}{file_ext}"
    file_path = os.path.join(UPLOAD_DIR, unique_filename)
    
    with open(file_path, "wb") as f:
        shutil.copyfileobj(photo.file, f)
    
    record = db.query(model.data).first()
    if record is None:
        record = model.data(photo=f"/uploads/{unique_filename}", cv=None)
        db.add(record)
    else:
        record.photo = f"/uploads/{unique_filename}"
    
    db.commit()
    db.refresh(record)
    
    return {
        "status": "success",
        "message": "Photo uploaded successfully",
        "photo": record.photo
    }

@app.post('/upload_cv')
def upload_cv(db: db_dependency, cv: UploadFile = File(...)): # type: ignore
    valid_types = ['application/pdf', 'application/msword', 
                   'application/vnd.openxmlformats-officedocument.wordprocessingml.document']
    
    if cv.content_type not in valid_types:
        return {"status": "error", "message": "Only PDF, DOC, DOCX files are allowed"}
    
    file_ext = os.path.splitext(cv.filename)[1]
    unique_filename = f"cv_{uuid.uuid4().hex}{file_ext}"
    file_path = os.path.join(UPLOAD_DIR, unique_filename)
    
    with open(file_path, "wb") as f:
        shutil.copyfileobj(cv.file, f)
    
    record = db.query(model.data).first()
    if record is None:
        record = model.data(photo=None, cv=f"/uploads/{unique_filename}")
        db.add(record)
    else:
        record.cv = f"/uploads/{unique_filename}"
    
    db.commit()
    db.refresh(record)
    
    return {
        "status": "success",
        "message": "CV uploaded successfully",
        "cv": record.cv
    }

@app.get('/get_files')
def get_files(db: db_dependency): # type: ignore
    record = db.query(model.data).first()
    if record is None:
        return {"photo": None, "cv": None}
    return {"photo": record.photo, "cv": record.cv}