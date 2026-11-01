# Hospital Management System

A web-based Hospital Management System built with Django to organize hospital operations and healthcare services.

## Planned Modules

- User authentication and role management
- Patient management
- Doctor and nurse management
- Department management
- Appointment management

Additional modules such as consultations, prescriptions, admissions, laboratory, pharmacy, billing, inventory, and reports will be added in later development phases.

## Tech Stack

- Python and Django
- Django Templates
- Tailwind CSS (frontend integration planned)
- Django REST Framework (API endpoints when needed)
- SQLite for initial local development; PostgreSQL planned for production

## Architecture

Modular Monolithic Architecture. Each business area is organized as a separate Django app under `apps/`.

## Project Status

🚧 Initial project scaffold. Features are not implemented yet.

## Getting Started

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py check
python manage.py migrate
python manage.py runserver
```

## Author

Mahibul Hasan — [@mahibulhasandev](https://github.com/mahibulhasandev)
