
# Job Tracker Web Application

A Django-based web application that allows users to manage and track their job applications efficiently. Users can register, log in, and perform full CRUD operations on job records with different application statuses.

---
## Tech Stack

* **Backend:** Django
* **Frontend:** HTML, CSS, Bootstrap
* **Database:** SQLite (local), PostgreSQL (production)
* **Deployment:** Render
* **Version Control:** Git & GitHub

---

## Features

* User authentication (Register, Login, Logout)
* Dashboard with job application statistics
* Add, edit, and delete job applications
* Search functionality by company or role
* Responsive UI using Bootstrap and custom CSS
* Admin panel for data management
* Hybrid database setup (SQLite for local development, PostgreSQL for production)
* Deployed on Render

---

## Setup (Local)

```bash
git clone <repository-url>
cd job-tracker
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## Deployment

The project is deployed on Render using environment variables and PostgreSQL for production.
Live Demo - https://job-tracker-8ogn.onrender.com/

---

This project was created for learning purposes and to gain hands-on experience with Django and backend web development.
