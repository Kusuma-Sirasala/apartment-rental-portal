# Residential Apartment Rental Portal

## Project Overview
This is a full-stack mini project built as part of an interview assignment.  
The application allows users to browse apartments, register/login, and request bookings.
An admin workflow is simulated via backend APIs.

---

## Tech Stack
- Frontend: Angular 20, HTML5, Tailwind CSS
- Backend: Python Flask (REST APIs)
- Database: PostgreSQL (schema-ready, mock data used)
- Authentication: JWT-based (backend-ready)
- Containerization: Docker & Docker Compose

---

## Project Structure
---

## Core Features

### User Portal
- User registration & login
- Browse available apartments
- View flat details and rent
- Request apartment booking
- Receive booking confirmation

### Admin (Mocked)
- Approve or decline bookings
- View occupancy status
- Manage apartment data (API-based)

---

## Backend APIs
| Method | Endpoint | Description |
|------|---------|-------------|
| POST | /api/register | User registration |
| POST | /api/login | User login |
| GET | /api/apartments | Fetch apartments |
| POST | /api/book | Book apartment |

---

## Running the Backend
```bash
cd backend
python app.py

