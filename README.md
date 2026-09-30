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
