# Brajesh Kumar Portfolio

A modern, responsive portfolio website built with FastAPI backend and vanilla JavaScript frontend.

## Features

- **Contact Form**: Visitors can send messages that are stored in PostgreSQL database
- **Project Showcase**: Display your projects with CRUD operations
- **Admin Dashboard**: Manage contacts and projects via API
- **Responsive Design**: Works on all devices with dark/light theme
- **Real-time Form Validation**: Client-side validation with loading states
- **API Documentation**: Auto-generated Swagger docs at `/docs`

## Tech Stack

### Backend
- **FastAPI**: High-performance async web framework
- **SQLAlchemy**: ORM for database operations
- **PostgreSQL**: Robust relational database
- **Pydantic**: Data validation and serialization

### Frontend
- **HTML5/CSS3**: Modern responsive design
- **Tailwind CSS**: Utility-first CSS framework
- **Vanilla JavaScript**: No frameworks, pure JS
- **Font Awesome**: Icons and UI elements

## API Endpoints

### Public Endpoints
- `GET /` - Welcome message and API status
- `POST /contact` - Submit contact form
- `GET /projects` - Get all projects for display

### Admin Endpoints (API)
- `GET /api/stats` - Get dashboard statistics
- `GET /api/contacts` - List all contact messages
- `DELETE /api/contacts/{id}` - Delete contact message
- `GET /api/projects` - List all projects
- `POST /api/projects` - Create new project
- `PUT /api/projects/{id}` - Update project
- `DELETE /api/projects/{id}` - Delete project

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd portfolio
   ```

2. **Backend Setup**
   ```bash
   cd backend
   python -m venv myenv
   myenv\Scripts\activate  # Windows
   pip install -r requirements.txt
   ```

3. **Database Setup**
   - Create PostgreSQL database
   - Update `db.env` with your database URL
   - Run the application to create tables automatically

4. **Run Backend**
   ```bash
   uvicorn app:app --reload
   ```

5. **Frontend Setup**
   ```bash
   cd frontend
   # Open home.html in browser or use live server
   ```

## Environment Variables

Create a `db.env` file in the backend directory:
```
url=postgresql://username:password@localhost:5432/portfolio
```

## Development

- **API Docs**: Visit `http://127.0.0.1:8000/docs` for interactive API documentation
- **Frontend**: Open `frontend/home.html` in your browser
- **Database**: Tables are created automatically on startup

## Production Deployment

For production deployment, consider:
- Using environment variables for configuration
- Adding authentication for admin endpoints
- Setting up proper CORS policies
- Adding rate limiting
- Using a production WSGI server (Gunicorn)
- Setting up proper logging

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License.</content>
<parameter name="filePath">c:\Users\hp\OneDrive\Desktop\profile\README.md