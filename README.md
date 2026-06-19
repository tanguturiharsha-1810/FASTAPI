# FastAPI Blog API

A RESTful Blog API built with FastAPI, PostgreSQL, SQLAlchemy, JWT Authentication, Docker, and Render Cloud Deployment.

## Live Deployment

### Production API

https://fastapi-blog-api-eksi.onrender.com

### Swagger Documentation

https://fastapi-blog-api-eksi.onrender.com/docs

### ReDoc Documentation

https://fastapi-blog-api-eksi.onrender.com/redoc

---

## Features

* User Registration
* User Authentication using JWT
* Password Hashing with Bcrypt
* User-Specific Blog Ownership
* Blog CRUD Operations
* PostgreSQL Database Integration
* SQLAlchemy ORM
* Interactive API Documentation (Swagger UI)
* Dockerized Application
* Docker Compose Support
* Docker Hub Image Publishing
* Environment Variable Configuration
* Cloud Deployment using Render
* Persistent Database Storage using Docker Volumes

---

## Tech Stack

* FastAPI
* PostgreSQL
* SQLAlchemy
* JWT Authentication
* Passlib (Bcrypt)
* Docker
* Docker Compose
* Docker Hub
* Render
* Neon PostgreSQL
* Uvicorn

---

## Deployment Architecture

```text
Client
   │
   ▼
Render Cloud Deployment
   │
   ▼
FastAPI Application
   │
   ▼
SQLAlchemy ORM
   │
   ▼
Neon PostgreSQL Database
```

---

## Project Structure

```text
blog/
├── auth/
│   ├── hashing.py
│   ├── oauth2.py
│   └── tokens.py
│
├── database/
│   └── database.py
│
├── models/
│   └── Models.py
│
├── repository/
│   ├── blog.py
│   └── user.py
│
├── router/
│   ├── authentication.py
│   ├── blog.py
│   └── user.py
│
├── schemas/
│   └── schemas.py
│
└── main.py

Dockerfile
docker-compose.yml
requirements.txt
```

---

## API Endpoints

### Authentication

| Method | Endpoint | Description                  |
| ------ | -------- | ---------------------------- |
| POST   | /login   | Login and generate JWT token |

### Users

| Method | Endpoint   | Description     |
| ------ | ---------- | --------------- |
| POST   | /user      | Create new user |
| GET    | /user/{id} | Get user by ID  |

### Blogs

| Method | Endpoint   | Description    |
| ------ | ---------- | -------------- |
| GET    | /blog      | Get all blogs  |
| GET    | /blog/{id} | Get blog by ID |
| POST   | /blog      | Create blog    |
| PUT    | /blog/{id} | Update blog    |
| DELETE | /blog/{id} | Delete blog    |

---

## Running with Docker

### Clone Repository

```bash
git clone https://github.com/tanguturiharsha-1810/FASTAPI.git
cd FASTAPI
```

### Build Containers

```bash
docker compose build
```

### Start Application

```bash
docker compose up -d
```

### Check Running Containers

```bash
docker ps
```

---

## Docker Hub

The application image is available on Docker Hub.

### Pull the Image

```bash
docker pull harshatanguturi1810/fastapi_postgresql:latest
```

### Run the Container

```bash
docker run -p 8000:8000 harshatanguturi1810/fastapi_postgresql:latest
```

### Verify the Container

```bash
docker ps
```

### Access the Application

FastAPI API:

```text
http://localhost:8000
```

Swagger UI:

```text
http://localhost:8000/docs
```

ReDoc Documentation:

```text
http://localhost:8000/redoc
```

### Docker Hub Repository

https://hub.docker.com/r/harshatanguturi1810/fastapi_postgresql

---

## Cloud Deployment

### Live Application

https://fastapi-blog-api-eksi.onrender.com

### Deployment Stack

* Render (Application Hosting)
* Neon PostgreSQL (Cloud Database)
* Docker (Containerization)
* Docker Hub (Image Registry)
* GitHub (Version Control)

### Deployment Features

* Automatic Deployment from GitHub
* Environment Variable Management
* Cloud PostgreSQL Database
* JWT Authentication
* Docker Container Deployment
* Public API Documentation

---

## Authentication Flow

1. Create a user using `/user`
2. Login using `/login`
3. Receive JWT access token
4. Click **Authorize** in Swagger UI
5. Access protected routes

---

## Project Highlights

* Developed a RESTful Blog API using FastAPI and PostgreSQL
* Implemented JWT Authentication and Authorization
* Secured Passwords using Bcrypt Hashing
* Built Complete CRUD Operations for Blogs and Users
* Implemented User-Specific Blog Ownership
* Containerized the Application using Docker and Docker Compose
* Published Docker Images to Docker Hub
* Configured Environment Variables for Secure Deployment
* Deployed the Application Publicly using Render
* Integrated Swagger/OpenAPI Documentation

---

## Future Improvements

* Alembic Database Migrations
* Role-Based Access Control (RBAC)
* Unit Testing with Pytest
* GitHub Actions CI/CD Pipeline
* Redis Caching
* API Rate Limiting
* Email Verification and Password Reset
* Custom Domain Deployment

---

## Author

**Tanguturi Harshavardhan Reddy**


