# Spatial Data Platform (Django + Docker)

A Django-based REST API for storing, updating, and retrieving **point** and **polygon spatial data**.  
This project uses **PostgreSQL** (with Docker) to store data and **Django REST Framework** for the API.  

---

## Features

Store and retrieve multiple **point** and **polygon** records.  
Perform CRUD operations (Create, Retrieve, Update, Delete).  
Store spatial data as JSON (no PostGIS dependency).  
Swagger documentation with interactive API testing.  
---

## Installation & Setup

### **1. Clone the Repository**
```bash
cd spatial-backend
python3 manage.py runserver
```
## API Endpoints

### Points API
    POST /api/points/ → Add new point
    GET /api/points/ → Retrieve all points
    GET /api/points/{id}/ → Retrieve single point
    PUT /api/points/{id}/ → Update point
    DELETE /api/points/{id}/ → Delete point

### Polygons API
    POST /api/polygons/ → Add new polygon
    GET /api/polygons/ → Retrieve all polygons
    GET /api/polygons/{id}/ → Retrieve single polygon
    PUT /api/polygons/{id}/ → Update polygon
    DELETE /api/polygons/{id}/ → Delete polygon
