# Late Show API

A Flask REST API to manage talk show guests, episodes, and appearances — complete with JWT authentication and PostgreSQL integration.

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd Phase-4-Code-Challenge-Two-Late-Show-API
```

### 2. Install Dependencies
```bash
pipenv install
pipenv shell
```

### 3. PostgreSQL Setup
Ensure PostgreSQL is installed and running.

Create the database:
```bash
sudo -u postgres psql
CREATE DATABASE late_show_db;
ALTER USER postgres WITH PASSWORD 'yourpassword';
\q
```

### 4. Set Up Environment Variables

Create a `.env` or `.flaskenv` file:
```
FLASK_APP=server.app:create_app
FLASK_ENV=development
```

Edit `server/config.py`:
```python
SQLALCHEMY_DATABASE_URI = "postgresql://postgres:yourpassword@localhost:5432/late_show_db"
```

---

## How to Run the Project

### 1. Initialize Database
```bash
flask db init
flask db migrate -m "initial"
flask db upgrade
```

### 2. Seed the Database
```bash
PYTHONPATH=. python server/seed.py
```

### 3. Start the Server
```bash
flask run
```

---

## Auth Flow

1. Register  
   `POST /register`  
   Body:
   ```json
   {
     "username": "admin",
     "password": "admin123"
   }
   ```

2. Login  
   `POST /login`  
   Returns a JWT token:
   ```json
   {
     "access_token": "eyJ0eXAiOiJKV1Qi..."
   }
   ```

3. Use JWT  
   For protected routes, set a header:
   ```
   Authorization: Bearer <your_token_here>
   ```

---

## Routes and Examples

| Route | Method | Auth | Description |
|-------|--------|------|-------------|
| `/register` | POST | No | Register a user |
| `/login` | POST | No | Log in and get JWT |
| `/episodes` | GET | No | List all episodes |
| `/episodes/<id>` | GET | No | Get one episode with appearances |
| `/episodes/<id>` | DELETE | Yes | Delete an episode |
| `/guests` | GET | No | List all guests |
| `/appearances` | POST | Yes | Create an appearance |

### Sample: Create Appearance (Requires Auth)
```http
POST /appearances
Authorization: Bearer <token>
Content-Type: application/json

{
  "rating": 4,
  "guest_id": 1,
  "episode_id": 2
}
```

---

## Postman Collection

Import this collection to test endpoints:

Download: `challenge-4-lateshow.postman_collection.json`

After login, your token will be saved to `{{token}}` and used in secured requests automatically.

---

## GitHub Repository

GitHub Repo: [https://github.com/Michael-Ngochi/Phase-4-Code-Challenge-Two-Late-Show-API.git](https://github.com/Michael-Ngochi/Phase-4-Code-Challenge-Two-Late-Show-API.git)

---

## Status

- Full CRUD for guests, episodes, and appearances
- JWT authentication and protected routes
- Database seeding and migration ready
- Postman collection provided for easy testing