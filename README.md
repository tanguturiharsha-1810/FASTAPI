# FastAPI Blog API

A RESTful Blog API built with FastAPI, PostgreSQL, SQLAlchemy, JWT Authentication, and Docker.

## Features

* User Registration
* User Authentication using JWT
* Password Hashing with Bcrypt
* Blog CRUD Operations
* PostgreSQL Database Integration
* SQLAlchemy ORM
* Interactive API Documentation (Swagger UI)
* Dockerized Application
* Docker Compose Support
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
* Uvicorn

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

```text
https://hub.docker.com/r/harshatanguturi1810/fastapi_postgresql
```


---


## Authentication Flow

1. Create a user using `/user`
2. Login using `/login`
3. Receive JWT access token
4. Click **Authorize** in Swagger UI
5. Access protected routes

---

## Future Improvements

* Alembic Database Migrations
* Environment Variables (.env)
* Role-Based Access Control
* Unit Testing with Pytest
* Blog Ownership and Permissions
* Cloud Deployment

---

## Author

**Tanguturi Harshavardhan Reddy**

Python Developer | FastAPI | PostgreSQL | Docker
