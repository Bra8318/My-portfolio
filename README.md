# Brajesh Kumar Portfolio

A modern, responsive portfolio website with FastAPI backend, PostgreSQL database, and vanilla JavaScript frontend. Features an admin dashboard for managing content and contact forms.

## 🚀 Features

- **Contact Management**: Visitors can send messages stored in PostgreSQL
- **File Upload System**: Upload and manage profile photo and CV through admin panel
- **Admin Dashboard**: Secure admin panel for managing contacts and files
- **Responsive Design**: Works on all devices with dark/light theme support
- **Real-time Validation**: Client-side form validation with loading states
- **API Documentation**: Auto-generated Swagger docs at `/docs`
- **File Serving**: Static file serving for uploaded content

## 🛠 Tech Stack

### Backend
- **FastAPI**: High-performance async web framework
- **SQLAlchemy**: ORM for database operations
- **PostgreSQL**: Robust relational database
- **Pydantic**: Data validation and serialization
- **python-multipart**: File upload handling

### Frontend
- **HTML5/CSS3**: Modern responsive design
- **Tailwind CSS**: Utility-first CSS framework
- **Vanilla JavaScript**: No frameworks, pure JavaScript
- **Font Awesome**: Icons and UI elements

## 📁 Project Structure

```
portfolio/
├── backend/
│   ├── app.py              # FastAPI application
│   ├── model.py            # SQLAlchemy models
│   ├── schema.py           # Pydantic schemas
│   ├── database.py         # Database configuration
│   ├── db.env              # Database environment variables
│   └── myenv/              # Virtual environment
├── frontend/
│   ├── home.html           # Main portfolio page
│   └── handle_request.html # Admin dashboard
└── uploads/                # Uploaded files (created automatically)
```

## 🗄 Database Schema

### Contacts Table
```sql
CREATE TABLE contacts (
    id SERIAL PRIMARY KEY,
    name VARCHAR,
    email VARCHAR,
    message TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Upload Files Table
```sql
CREATE TABLE upload_file (
    id SERIAL PRIMARY KEY,
    photo VARCHAR,
    cv VARCHAR
);
```

## 🔗 API Endpoints

### Public Endpoints
- `GET /` - Welcome message
- `POST /contact` - Submit contact form
- `GET /get_files` - Get uploaded photo and CV paths
- `GET /uploads/{filename}` - Serve uploaded files

### Admin Endpoints
- `GET /show_contacts` - List all contact messages
- `POST /delete_contacts/{id}` - Delete contact message
- `POST /upload_photo` - Upload profile photo
- `POST /upload_cv` - Upload CV/resume

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- PostgreSQL
- Git

### 1. Clone Repository
```bash
git clone https://github.com/Bra8318/My-portfolio.git
cd My-portfolio
```

### 2. Backend Setup
```bash
cd backend

# Create virtual environment
python -m venv myenv
myenv\Scripts\activate  # Windows
# source myenv/bin/activate  # Linux/Mac

# Install dependencies
pip install fastapi uvicorn sqlalchemy psycopg2-binary python-dotenv python-multipart

# Setup database
# Create PostgreSQL database and update db.env
```

### 3. Database Configuration
Create `backend/db.env`:
```
url=postgresql://username:password@localhost:5432/portfolio_db
```

### 4. Run Backend
```bash
uvicorn app:app --reload --host 127.0.0.1 --port 8000
```

### 5. Frontend
Open `frontend/home.html` in your browser or use a live server.

## 🔐 Admin Panel Access

1. Open `frontend/handle_request.html`
2. Login with credentials:
   - **Username**: `admin`
   - **Password**: `admin123`
3. Manage contacts and upload files

## 📋 Usage

### For Visitors
- View portfolio at `home.html`
- Download CV using the download button
- Send contact messages via the form

### For Admin
- Access admin panel at `handle_request.html`
- Upload profile photo and CV
- View and delete contact messages
- Files are automatically served and updated on the main site

## 🔧 Development

### API Documentation
Visit `http://127.0.0.1:8000/docs` for interactive API documentation.

### File Upload Limits
- **Photo**: Max 5MB, Images only (JPEG, PNG, etc.)
- **CV**: Max 10MB, PDF, DOC, DOCX only

### Environment Variables
```env
url=postgresql://user:password@host:port/database
```

## 🚀 Production Deployment

### Backend Deployment
```bash
# Install production server
pip install gunicorn

# Run with Gunicorn
gunicorn app:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

### Frontend Deployment
- Host static files on any web server
- Update API URLs to production backend
- Configure CORS for production domain

### Security Considerations
- Add authentication for admin endpoints
- Use HTTPS in production
- Validate file uploads server-side
- Set up proper CORS policies
- Add rate limiting
- Use environment variables for sensitive data

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 📞 Contact

Brajesh Kumar
- Email: brajeshkumar23390@gmail.com
- LinkedIn: [Brajesh Kumar](https://www.linkedin.com/in/brajesh-kumar-20g)
- GitHub: [@Bra8318](https://github.com/Bra8318)

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License.</content>
<parameter name="filePath">c:\Users\hp\OneDrive\Desktop\profile\README.md