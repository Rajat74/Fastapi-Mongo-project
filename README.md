# FastAPI and MongoDB Project

## Table of Contents

1. [Introduction](#introduction)
2. [Project Setup](#project-setup)
3. [Environment Variables](#environment-variables)
4. [API Endpoints](#api-endpoints)
    - [User Registration](#user-registration)
    - [User Login](#user-login)
    - [Linking ID](#linking-id)
    - [Join Data](#join-data)
    - [Chain Delete](#chain-delete)
5. [Database Schema](#database-schema)
6. [Usage Examples](#usage-examples)
7. [Running the Application](#running-the-application)

## Introduction

This project is a web application built using FastAPI and MongoDB. It provides APIs for user registration, login, linking an ID to a user account, joining data from multiple collections, and deleting a user along with all associated data.

## Project Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-repo/fastapi-mongo-project.git
    cd fastapi-mongo-project
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Create a `.env` file in the root directory and add the following variables:**

## Environment Variables

Create a `.env` file in the root directory and add the following variables:
``MONGODB_URI="your_mongodb_uri"``
``SECRET_KEY="your_secret_key"``

## API Endpoints

### User Registration

- **Endpoint:** `/users/register`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
        "username": "exampleUser",
        "email": "user@example.com",
        "password": "password123"
    }
    ```
- **Response:**
    ```json
    {
        "id": "60c72b2f5f1b2c6d88d0f6e4",
        "username": "exampleUser",
        "email": "user@example.com"
    }
    ```

### User Login

- **Endpoint:** `/users/login`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
        "email": "user@example.com",
        "password": "password123"
    }
    ```
- **Response:**
    ```json
    {
        "access_token": "jwt_token_here",
        "token_type": "bearer"
    }
    ```

### Linking ID

- **Endpoint:** `/link`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
        "user_id": "60c72b2f5f1b2c6d88d0f6e4",
        "external_id": "external_id_12345"
    }
    ```
- **Response:**
    ```json
    {
        "message": "ID linked successfully"
    }
    ```

### Join Data

- **Endpoint:** `/join`
- **Method:** `GET`
- **Description:** This endpoint is for joining data from multiple collections. (Implement this as needed based on your data structure.)

### Chain Delete

- **Endpoint:** `/users/{user_id}`
- **Method:** `DELETE`
- **Description:** This endpoint deletes a user and all associated data across collections. (Implement this as needed based on your data structure.)

## Database Schema

### User Collection

```json
{
    "_id": "ObjectId",
    "username": "string",
    "email": "string",
    "password": "string",
    "external_id": "string (optional)"
}
```

## Usage Examples

### Register a User

```bash
curl -X POST "http://127.0.0.1:8000/users/register" -H "Content-Type: application/json" -d '{
    "username": "exampleUser",
    "email": "user@example.com",
    "password": "password123"
}'
```
### Login a User

```bash
curl -X POST "http://127.0.0.1:8000/users/login" -H "Content-Type: application/json" -d '{
    "email": "user@example.com",
    "password": "password123"
}'
```

### Link an ID

```bash
curl -X POST "http://127.0.0.1:8000/link" -H "Content-Type: application/json" -d '{
    "user_id": "60c72b2f5f1b2c6d88d0f6e4",
    "external_id": "external_id_12345"
}'
```
## Running the Application

To run the FastAPI application, use the following command:

```bash
uvicorn app.main:app --reload
```
