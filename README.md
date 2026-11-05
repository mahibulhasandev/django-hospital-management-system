# Hospital Management System

A Django-based Hospital Management System designed to manage hospital operations, users, departments, doctors, and patient information through a centralized platform.

## Project Overview

This project aims to simplify hospital administration by providing role-based access and organized management of hospital resources.

**Project Status:** 🚧 Under Development

## Technology Stack

- **Backend:** Python, Django
- **Frontend:** Django Templates, HTML, Tailwind CSS
- **Database:** SQLite (Development), PostgreSQL (Planned)
- **Version Control:** Git & GitHub

## Current Features

- Custom User Model
- Role-Based Authentication
- Email or Phone Number Login
- User Roles:
  - Hospital Admin
  - Doctor
  - Nurse
  - Receptionist
  - Staff
  - Patient
  - Laboratory Technician
  - Pharmacist
- Patient Self-Registration
- Patient Profile Management
- Role-Based Dashboards
- Department Management (CRUD)
- Doctor Management (CRUD)
- Doctor Department Assignment
- Doctor Availability Management

## Upcoming Features

- Nurse Management
- Appointment Management
- Receptionist Panel
- Doctor Scheduling
- Patient Medical Records
- Prescription Management
- Laboratory Management
- Pharmacy Management
- Billing & Payment Management
- Reports & Analytics

## Project Structure

```text
django-hospital-management-system/
├── apps/
│   ├── accounts/
│   ├── appointments/
│   ├── departments/
│   ├── doctors/
│   ├── nurses/
│   └── patients/
├── common/
├── config/
│   └── settings/
├── docs/
├── templates/
├── static/
├── media/
├── tests/
├── manage.py
├── requirements.txt
└── README.md
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/mahibulhasandev/django-hospital-management-system.git

cd django-hospital-management-system
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

Activate on Linux:

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Create Superuser

```bash
python manage.py createsuperuser
```

### 6. Run Development Server

```bash
python manage.py runserver
```

Open: `http://127.0.0.1:8000/`

## Development Approach

The project follows a modular monolithic architecture using Django applications. Each major hospital management feature is organized into a separate app for better maintainability and scalability.

## Author

**Mahibul Hasan**

- GitHub: [@mahibulhasandev](https://github.com/mahibulhasandev)

---

*This project is being developed for learning and practical implementation of Django-based web application development.*