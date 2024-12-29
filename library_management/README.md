# Library Management System

---- This project is a **Library Management System** built using Django and sqlite3 (inbuilt database), designed to manage books, members, and borrow/return records. The system provides RESTful APIs for managing library operations efficiently.

# Features
---- Books Management
---- Members Management
---- Borrow and Return Records
---- JSON Response

# Technologies Used

---- Framework      : Django Rest Framework (DRF)
---- Database       : SQLite3 (In built of Django)
---- Python Version : 3.10

# Steps For Running this Project

---- python -m venv library_env
---- source venv/bin/activate (For Linux)
---- pip install -r requirements.txt
---- Migration Command :  
            python manage.py makemigrations
            python manage.py migrate
---- python manage.py runserver

# API Endpoints

1.  List Books
    http://127.0.0.1:8000/books/                (GET Request)
    Example : http://127.0.0.1:8000/books/?title=********&author=******&category=****** (For Filteration)

2.  Add a Book
    http://127.0.0.1:8000/books/add/            (POST Request)
    payload : {
        "title" : "Hindi Literature",
        "author" : "Shivam Gupta",
        "category" : "Hindi Books",
        "published_date" : "2024-12-29",
        "available_copies" : 10
    }

3.  List Members
    http://127.0.0.1:8000/members/               (GET Request)

4.  Register a Member
    http://127.0.0.1:8000/members/add/           (POST Request)
    payload : {
        "name" : "Mr. Raj",
        "email" : "rajkumar@gmail.com",
        "membership_date" : "2024-12-28"
    }

5.  Borrow a Book
    http://127.0.0.1:8000/borrow/                (POST Request)
    payload : {
        "member": 1,
        "book": 1,
        "borrow_date": "2024-12-29"
    }

6.  Return a Book
    http://127.0.0.1:8000/return/<int:pk>/       (POST Request)