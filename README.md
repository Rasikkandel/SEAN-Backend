SEAN Backend  
A  Django-based backend system built for the SEAN Tech Club platform.
This project is designed to handle core backend responsibilities such as user management, content handling (blogs, projects, resources), and to serve as a foundation for a scalable REST API–driven application.

The goal of this project is to provide a clean, maintainable, and extensible backend that can power a tech community platform where users can publish blogs, showcase projects, and share resources.

This project focuses on:
Proper backend structure
Separation of concerns using Django apps
Clean database modeling
API-ready architecture for future frontend integration

🛠️ Tech Stack

Language: Python
Framework: Django
Backend Architecture: App-based modular design
Database: Django ORM 
Dependency Management: requirements.txt
Version Control: Git & GitHub
######
📂 Project Structure
SEAN-Backend/
├── SEAN/                 # Main project settings and configuration
├── USer/                 # User management and authentication logic
├── blogs/                # Blog-related models and logic
├── projects/             # Project-related backend logic
├── resources/            # Resource management
├── manage.py             # Django management utility
├── requirements.txt      # Project dependencies
├── LICENSE
└── README.md


This structure follows Django’s recommended architecture, allowing the project to scale easily as new features or APIs are added.

⚙️ Features
Core Features

User management using Django’s authentication system
Backend logic for blogs, projects, and resources
Clean separation of features using Django apps
Database handling using Django ORM
API-ready structure for future REST integration


Planned Enhancements

Full REST API using Django REST Framework
Token-based authentication
Role-based permissions (admin, members, public users)
Frontend integration (React or similar)

🚀 Installation & Setup

Follow these steps to run the project locally:

1. Clone the Repository
git clone https://github.com/Rasikkandel/SEAN-Backend.git
cd SEAN-Backend

2. Create and Activate Virtual Environment
python -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate         # Windows

3. Install Dependencies
pip install -r requirements.txt

4. Apply Database Migrations
python manage.py makemigrations
python manage.py migrate

5. Run the Development Server
python manage.py runserver


📄 License
This project is licensed under the MIT License.

👤 Author

Rasik Kandel
Backend Developer | Django
