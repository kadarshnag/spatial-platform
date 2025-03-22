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

## Sample Payloads
### Point Payload
    {
        "name": "Central Park",
        "coordinates": {
            "latitude": 40.785091,
            "longitude": -73.968285
        }
    }

### Polygon Payload
    {
        "name": "Washington DC Area",
        "coordinates": {
            "type": "Polygon",
            "coordinates": [
                [
                    [-77.03653, 38.897676],
                    [-77.009051, 38.889939],
                    [-77.015083, 38.881258],
                    [-77.03653, 38.897676]
                ]
            ]
        }
    }