# DriveNest — Smart Car Rental Platform

DriveNest is a portfolio-ready Django car rental platform rebuilt from the original CarZest concept. It combines a responsive frontend with account-based reservations, server-side pricing, fleet discovery and practical booking management.

## What makes this version stronger

- Rebranded product experience: **DriveNest**
- Modern responsive landing page and navigation
- Database-driven fleet with category, seats, transmission, fuel type and availability metadata
- Fleet search, filtering and sorting
- Account dashboard with booking statistics and recent activity
- Booking history with unique references such as `DN-00001`
- Booking cancellation workflow
- Server-side rental total calculation
- Server-side date-overlap protection to prevent conflicting active reservations
- Pickup and return dates stored separately for cleaner booking logic
- Improved Django admin for fleet and booking operations
- Automated tests for authentication, filtering, pricing, date calculations, conflict detection and cancellation
- Environment-based Django secret key and host configuration

> **Project scope:** This is a student/portfolio project. It does not process real payments or operate a live commercial fleet.

## Core features

### Customer side
- Registration and login
- Responsive homepage
- Fleet search and filters
- Vehicle detail metadata
- Booking form with live price preview
- Date validation
- Booking conflict validation
- Personal dashboard
- Booking history
- Booking cancellation
- Contact form

### Admin side
- Add/edit/remove vehicles
- Mark vehicles available/unavailable
- Filter fleet by category, fuel and transmission
- Search and manage bookings
- Update booking status
- Review customer contact messages

## Tech stack

- **Backend:** Python, Django 5.2
- **Frontend:** HTML, CSS, Bootstrap 5, Bootstrap Icons, JavaScript
- **Database:** SQLite for local development
- **Image handling:** Pillow
- **Testing:** Django TestCase

## Project structure

```text
DriveNest/
├── MyApp/
│   ├── migrations/
│   ├── admin.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── vehicles/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── static/
├── templates/
├── fixtures/
├── .env.example
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

## Run locally

### 1. Create a virtual environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Apply migrations

```bash
python manage.py migrate
```

### 4. Load the demo fleet

```bash
python manage.py loaddata fixtures/cars.json
```

### 5. Create an admin user

```bash
python manage.py createsuperuser
```

### 6. Start the server

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/`.

Admin: `http://127.0.0.1:8000/admin/`

## Test suite

```bash
python manage.py test
```

## Portfolio talking points

If you present DriveNest in an interview, the strongest technical points are:

1. **Server-side pricing:** the client-side total is only a preview; the backend calculates the final amount from the database price.
2. **Booking conflict detection:** active reservations are checked for overlapping pickup/return windows before a booking is created.
3. **Authentication and ownership:** users can only access and cancel their own bookings.
4. **Query-driven fleet discovery:** Django ORM filters the fleet by search text, category, transmission, fuel and price ordering.
5. **Admin workflow:** fleet availability and booking statuses can be managed without editing code.
6. **Automated tests:** core booking rules are covered by Django TestCase tests.

## Future production upgrades

- PostgreSQL
- Payment gateway integration
- Email/SMS confirmations
- Redis/Celery for background jobs
- REST API / mobile client
- Docker + CI/CD
- Cloud object storage for vehicle images
- Role-based staff dashboard
- Real-time fleet availability calendar


## 🛠️ Tech Stack

Python
Django
SQLite
HTML
CSS
JavaScript

## 📸 Screenshots

## ⚙️ Installation

## 🚀 Running Locally

## 📂 Project Structure

## 🔮 Future Improvements

## Attribution

The original project was a student/hackathon-style Django car rental application. Before publishing publicly, retain any required attribution or license information from the source repository.
