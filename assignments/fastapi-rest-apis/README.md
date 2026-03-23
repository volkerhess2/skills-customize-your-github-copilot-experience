# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build modern REST APIs using the FastAPI framework. You'll create a fully functional API with request validation, response models, and database integration, understanding core web development concepts including HTTP methods, routing, and data serialization.

## 📝 Tasks

### 🛠️ Create a Basic REST API

#### Description

Build a basic REST API using FastAPI with multiple endpoints that handle CRUD operations (Create, Read, Update, Delete). Your API should use Python data classes or Pydantic models to define request and response schemas, and implement error handling for invalid requests.

#### Requirements

Completed program should:

- Define at least 3 API endpoints using appropriate HTTP methods (GET, POST, PUT, DELETE)
- Use Pydantic models for request and response validation
- Implement proper HTTP status codes (200, 201, 400, 404, etc.)
- Include error handling for missing resources and invalid input
- Document endpoints with docstrings

### 🛠️ Add Data Persistence and Advanced Features

#### Description

Extend your REST API to include database integration for persistent data storage. Implement filtering, pagination, and query parameters to make your API more robust and production-ready.

#### Requirements

Completed program should:

- Integrate with a database (SQLite or similar) for data persistence
- Implement filtering and search functionality using query parameters
- Add pagination support to list endpoints (limit and offset)
- Include request validation using Pydantic with appropriate error messages
- Add dependency injection for code reusability (e.g., database sessions)
