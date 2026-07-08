# Inventory Purchase & Vendor Management System

## Project Overview

The Inventory Purchase & Vendor Management System is a backend REST API developed using **FastAPI**. It allows administrators and store managers to manage vendors, purchase orders, authentication, reports, and inventory purchasing operations securely using JWT Authentication.

---

## Objective

Develop a secure backend application with:

- User Authentication
- Role-Based Authorization
- Vendor Management
- Purchase Order Management
- Reports & Search
- Pagination
- Business Rule Validation

---

## Technology Stack

- Python 3.11
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- JWT Authentication
- Uvicorn
- Passlib (bcrypt)
- Pytest

---

## Project Structure

```
inventory_purchase_vendor_management_system/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── auth.py
├── oauth2.py
├── dependencies.py
├── utils.py
├── inventory.db
├── requirements.txt
├── README.md
│
├── routers/
│   ├── __init__.py
│   ├── auth.py
│   ├── vendors.py
│   ├── purchase_orders.py
│   └── reports.py
│
└── tests/
    ├── conftest.py
    ├── test_auth.py
    ├── test_vendor.py
    ├── test_purchase_order.py
    └── test_reports.py
```

---

# Features

## Authentication

- User Registration
- User Login
- JWT Token Authentication

---

## User Roles

### Admin

- Register Users
- Manage Vendors
- Manage Purchase Orders
- View Reports

### Store Manager

- Manage Purchase Orders
- View Reports

---

## Vendor Management

- Create Vendor
- Get All Vendors
- Get Vendor by ID
- Update Vendor
- Soft Delete Vendor

---

## Purchase Order Management

- Create Purchase Order
- Get All Purchase Orders
- Get Purchase Order by ID
- Update Purchase Order

---

## Reports

- Purchase History by Vendor
- Filter Orders by Status
- Search Orders by Product Name
- Pagination

---

# Business Rules

- Vendor Email must be Unique.
- Quantity must be greater than 0.
- Unit Price must be greater than 0.
- Total Amount is calculated automatically.
- Purchase Orders cannot be created for inactive Vendors.
- Received Purchase Orders cannot be updated.
- Soft Delete for Vendors using `is_active`.

---

# API Endpoints

## Authentication

| Method | Endpoint |
|---------|----------|
| POST | /auth/register |
| POST | /auth/login |

---

## Vendor APIs

| Method | Endpoint |
|---------|----------|
| POST | /vendors |
| GET | /vendors |
| GET | /vendors/{id} |
| PUT | /vendors/{id} |
| DELETE | /vendors/{id} |

---

## Purchase Order APIs

| Method | Endpoint |
|---------|----------|
| POST | /purchase-orders |
| GET | /purchase-orders |
| GET | /purchase-orders/{id} |
| PUT | /purchase-orders/{id} |

---

## Reports APIs

| Method | Endpoint |
|---------|----------|
| GET | /reports/vendor/{vendor_id} |
| GET | /reports/status/{status} |
| GET | /reports/search |
| GET | /reports/pagination |

---

# Installation

## Clone Repository

```bash
git clone https://github.com/your-username/inventory_purchase_vendor_management_system.git
```

---

## Go to Project Folder

```bash
cd inventory_purchase_vendor_management_system
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
uvicorn main:app --reload
```

---

# Swagger Documentation

Open:

```
http://127.0.0.1:8000/docs
```

---

# Running Tests

Run all tests:

```bash
python -m pytest
```

Run with verbose output:

```bash
python -m pytest -v
```

---

# Database

SQLite Database

```
inventory.db
```

---

# Authentication

The project uses **JWT Bearer Token Authentication**.

1. Register User
2. Login
3. Copy JWT Token
4. Click **Authorize** in Swagger
5. Enter:

```
Bearer <your_token>
```

---

# Sample Admin Account

```
Email:
admin@gmail.com

Password:
admin123

Role:
Admin
```

---

# Author

**Name:** Your Name

Backend Developer

FastAPI | Python | SQLAlchemy

---

# License

This project is developed for educational and learning purposes.
