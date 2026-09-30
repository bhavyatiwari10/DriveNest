# 🚗 DriveNest - Django Car Rental System

DriveNest is a Django-based car rental web application originally built as a collaborative hackathon project and later shared on a teammate's GitHub repository. This repository is a refreshed and enhanced version of that project, retaining the original concept while improving the backend, booking flow, security configuration, frontend experience, database-driven vehicle management, testing, and deployment readiness.

> **Project Note:** This is a student/portfolio project designed to demonstrate full-stack web development skills. It is not intended to operate as a production rental marketplace. Real-world payment processing, live fleet tracking, advanced availability synchronization, and commercial fleet operations are outside the current scope.

## 🌐 Live Demo

**DriveNest Live Application:**  
https://drivenest-vpaq.onrender.com/

**GitHub Repository:**  
https://github.com/bhavyatiwari10/DriveNest

---

## ✨ What Changed in the Refreshed Version

The original application was significantly cleaned up and enhanced for portfolio use.

- Modern responsive UI with a redesigned landing page
- Improved fleet cards and vehicle presentation
- Database-driven vehicle listings instead of hard-coded vehicle choices
- Login-protected fleet and booking pages
- User-specific **My Bookings** history
- User dashboard with booking statistics
- Server-side rental-price calculation
- Booking duration and date validation
- Booking conflict prevention for overlapping reservations
- Booking cancellation functionality
- Django admin improvements for vehicles, bookings and contact messages
- Environment-based Django secret key configuration
- Environment-based allowed-host configuration
- Production-ready static-file handling using WhiteNoise
- Clean `.gitignore` to prevent local and sensitive files from being committed
- Demo vehicle fixture for quick setup
- Automated tests covering authentication, vehicle access and booking calculations
- GitHub-based version control
- Render deployment configuration

---

## Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, Bootstrap 5, Bootstrap Icons, JavaScript
- **Database:** SQLite for local development
- **Image handling:** Pillow
- **Testing:** Django TestCase

## Project Structure

```text
Car-Rental-System/
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
├── .env.example
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

# 🚘 Features

## 👤 User Authentication

DriveNest uses Django's authentication system to provide protected user functionality.

Users can:

- Register an account
- Log in
- Log out
- Access protected pages
- Make vehicle bookings
- View their own booking history
- Cancel eligible bookings

---

## 🚗 Vehicle Fleet

Users can browse a database-driven fleet of rental vehicles.

Each vehicle can contain:

- Vehicle ID
- Vehicle name
- Description
- Daily rental price
- Vehicle image
- Number of seats
- Category
- Transmission
- Fuel type
- Availability status

Vehicle information is retrieved dynamically from the database rather than being hard-coded into the frontend.

---

## 🔎 Fleet Search, Filtering & Sorting

Users can discover vehicles using fleet search and filtering functionality.

Supported options include:

- Vehicle name
- Vehicle category
- Fuel type
- Transmission
- Price
- Availability

Vehicles can also be sorted according to rental price.

---

## 📅 Vehicle Booking

Authenticated users can select a vehicle and choose:

- Pickup date
- Return date

The system automatically calculates the rental duration and total rental cost.

Example:

```text
Daily Rental Price = ₹2,000
Rental Duration = 3 Days

Total Rental Cost
= ₹2,000 × 3
= ₹6,000
```

## License
## Original Project Context & Credits

DriveNest was originally a collaborative car rental project built by **me and my friend Bharat**. This repository is my enhanced and reworked version of that project. The original concept has been retained, and I worked on the following improvements:
- Rebranded and redesigned the project as **DriveNest**
- Replaced static vehicle selections with database-driven fleet listings
- Added vehicle search, filtering, sorting and detailed vehicle information
- Added user authentication and a dedicated **My Bookings** dashboard
- Added booking references, pickup/return dates and booking cancellation
- Implemented server-side rental-price calculation and booking validation
- Added date-overlap protection to prevent conflicting vehicle bookings
- Improved Django Admin for managing vehicles and bookings
- Added automated tests for authentication, vehicle access and booking logic
- Rebuilt and improved the frontend for a cleaner, responsive user experience
- Added environment-based configuration for Django settings and allowed hosts
- Added production static-file handling using **WhiteNoise**
- Added database fixtures for quick fleet setup and deployment
- Deployed the application online using **Render**

## Future Improvements

Potential next steps include:

- Real-time vehicle availability
- Payment gateway integration
- Booking cancellation and refund workflows
- Email/SMS booking confirmations
- PostgreSQL for production deployment
- Docker-based deployment
- REST API for a mobile client
- Automated CI/CD with GitHub Actions


