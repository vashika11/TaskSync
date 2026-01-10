# TaskSync – Task Management Web Application

TaskSync is a modern, lightweight task management web application developed using Python (Flask) and SQLite.  
It provides a clean and intuitive interface that allows users to securely manage tasks with support for descriptions, timestamps and a professional dashboard experience.

The application is designed with a strong focus on clarity, maintainability and usability, making it suitable for real-world usage and future extension.


## Features

### Authentication
- User registration
- User login with session handling
- Secure logout
- User-specific data isolation

### Task Management
- Create tasks with:
  - Title
  - Description (optional)
  - Automatically generated creation date and time
- View tasks in a structured dashboard
- Edit existing tasks
- Delete tasks

### User Interface
- Modern and elegant login and registration pages
- Clean, medium-sized dashboard layout
- Dark mode toggle


## Technology Stack

- Python
- Flask
- HTML5
- CSS3
- SQLite
- Flask Sessions


## Application Details

- Application Type: Web Application  
- Architecture: Monolithic  
- Backend Framework: Flask  
- Database Type: SQLite (file-based)


## Project Structure

  
   TaskSync/
   ├── app.py
   ├── database.db
   ├── requirements.txt
   ├── README.md
   ├── templates/
   │ ├── login.html
   │ ├── register.html
   │ ├── dashboard.html
   │ └── edit.html
   └── static/
   └── style.css


## Setup Steps

1. Download or clone the repository
2. Navigate to the project folder
3. Install dependencies  
   ```bash
   pip install -r requirements.txt
4. Run the application
   ```bash
   python app.py
5. Open your browser and visit
   ```bash
   http://127.0.0.1:5000
   
## Notes

- SQLite database is auto-created on first run
- No manual database setup required


## Author
Vashika Tyagi