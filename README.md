# Hospital Management System

A Django-based Hospital Management System (HMS) designed to organize hospital operations through a centralized, role-based platform. The project is being developed with a modular Django architecture and server-rendered Django templates.

> **Project Status:** Under Development 🚧

## Project Overview

The goal of this project is to provide a centralized system for managing hospital users, departments, doctors, patients, appointments, and other operational workflows.

The application uses separate Django apps for major functional areas. This keeps responsibilities organized and makes the system easier to maintain and extend.

## Technology Stack

| Area | Technology |
|---|---|
| Backend | Python, Django |
| Frontend | Django Templates, HTML, Tailwind CSS |
| API | Django REST Framework |
| Development Database | SQLite |
| Planned Production Database | PostgreSQL |
| Version Control | Git and GitHub |

## Current Features

### Accounts and Authentication

- Custom Django User Model
- Role-Based Authentication
- Email or Phone Number Login
- Role-Based Dashboards
- Patient Self-Registration
- Patient Account Management
- Staff Registration Workflow (In Progress)
- Hospital Admin Staff Approval Workflow (In Progress)

### Available User Roles

- Hospital Admin
- Doctor
- Nurse
- Receptionist
- Staff
- Patient
- Laboratory Technician
- Pharmacist

### Departments

- Department Management
- Create, Read, Update, and Delete (CRUD)
- Department Assignment to Doctors

### Doctors

- Doctor Management
- Doctor Profile Management
- Doctor Department Assignment
- Doctor Specialization
- Qualification and Experience Information
- Consultation Fee Management
- Doctor Availability Management
- Doctor Scheduling (In Progress)

### Staff Registration Workflow

The planned staff registration workflow allows applicants to register by selecting one of the following roles:

- Doctor
- Nurse
- Receptionist
- Staff

The registration request will remain pending until the Hospital Admin reviews it.

For Doctor registration, applicants provide:

- Department
- Specialization
- Qualification
- Experience Years
- Consultation Fee

After approval, the applicant's account will be activated and the requested role will be assigned.

> Staff approval, rejection, and account activation are still under development and require complete workflow testing.

## Upcoming Features

- Complete Staff Approval and Rejection System
- Nurse Management
- Doctor Schedule Management
- Appointment Management
- Receptionist Panel
- Patient Medical Records
- Prescription Management
- Laboratory Management
- Pharmacy Management
- Billing and Payment Management
- Reports and Analytics
- REST API Development

## Project Structure

```text
django-hospital-management-system/
│
├── apps/
│   ├── accounts/
│   ├── appointments/
│   ├── departments/
│   ├── doctors/
│   ├── nurses/
│   └── patients/
│
├── common/
├── config/
│   └── settings/
│
├── docs/
├── templates/
├── static/
│   ├── css/
│   └── src/
│
├── media/
├── tests/
│
├── manage.py
├── package.json
├── requirements.txt
└── README.md
```

## Installation and Setup

### Prerequisites

Make sure you have installed:

- Python
- Node.js
- npm
- Git

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

Activate on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Node Dependencies

```bash
npm install
```

### 5. Start Tailwind CSS

The current Tailwind CSS file locations are:

**Input CSS:**

```text
static/src/input.css
```

**Output CSS:**

```text
static/css/style.css
```

Run the Tailwind CLI in watch mode:

```bash
npx @tailwindcss/cli -i ./static/src/input.css -o ./static/css/style.css --watch
```

Keep this terminal running during development.

### 6. Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

For a specific app:

```bash
python manage.py makemigrations accounts
```

### 7. Create Superuser

```bash
python manage.py createsuperuser
```

### 8. Run Development Server

Open another terminal and run:

```bash
python manage.py runserver
```

Open your browser:

**Application:**

http://127.0.0.1:8000/

**Django Admin:**

http://127.0.0.1:8000/admin/

## Development Workflow

For local development, use two separate terminals.

**Terminal 1 — Tailwind CSS**

```bash
npx @tailwindcss/cli -i ./static/src/input.css -o ./static/css/style.css --watch
```

**Terminal 2 — Django Development Server**

```bash
python manage.py runserver
```

Whenever you modify Django models, run:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Architecture

The project follows a **Modular Monolithic Architecture** using Django applications.

Each app handles a specific functional area of the hospital management system.

| Django