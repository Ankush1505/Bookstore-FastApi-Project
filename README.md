# 📚 FastAPI Bookstore API

This is a backend API built to manage an online bookstore. I built this project to move beyond basic Python scripts and master professional backend architecture using **FastAPI**, **PostgreSQL**, and **Docker/Render**.

🚀 **Live Demo:** Click here to view the Swagger UI ->
(https://bookstore-fastapi-ankush.onrender.com/docs)
*(Note: Hosted on a free Render instance. Please allow 30-50 seconds for the server to wake up if it is sleeping.)*

----------------

## ==> 💡 What I Learned
This project was my transition from "coding" to "software engineering." I wanted to understand how data flows in a real production application.

* **Authentication Architecture:** I learned to separate logic into two parts: `auth.py` handles the login (generating the JWT), while `oauth2.py` acts as the "guard" that verifies the token on every request.
* **ORM vs Raw SQL:** I used **SQLAlchemy** to manage database interactions, which made handling relationships (like Users and their Votes) much cleaner than writing raw SQL strings.
* **Environment Security:** I learned the importance of hiding secrets. The app uses a `.env` file locally and Environment Variables in the cloud to protect the Database Password and Secret Keys.

---------------

## ==> 🛠️ Tech Stack
* **Language:** Python.
* **Framework:** FastAPI.
* **Database:** PostgreSQL. (Hosted on Render)
* **ORM:** SQLAlchemy.
* **Authentication:** JWT (JSON Web Tokens) with OAuth2
* **Deployment:** Render (CI/CD pipeline via GitHub)

----------------

## ==> ⚡ Key Features

* **User Authentication:** Secure Signup & Login with password hashing (Bcrypt).
* **CRUD Operations:** Create, Read, Update, and Delete books.
* **Vote/Like System:** Users can vote on books (similar to a "Like" button).
* **Documentation:** Interactive API documentation (Swagger UI) included automatically.

----------------

## ==> 🔐 How Authentication Works

This API uses **OAuth2 with Password Flow** and **JWT Tokens**.

1. **User Registration:** Passwords are hashed using **Bcrypt** before being stored in the database.
2. **Login:** Users send `email` + `password` to the `/login` endpoint.
3. **Token:** If valid, the server returns a **JWT Access Token**.
4. **Access:** To access protected routes (like `POST /books`), the user must send the token in the request header:
   `Authorization: Bearer <your_token>`

------------------

## ==> 📂 Project Structure

* `main.py`: The entry point of the application.
* `models.py`: Defines the Database Tables (SQLAlchemy models).
* `schemas.py`: Defines the Data Validation (Pydantic models) - keeps bad data out.
* `routers/`: Splits the code into organised modules (`auth.py`, `books.py`, `user.py`, `vote.py`).
* `oauth2.py`: Handles token verification logic.

-------------------

## ==> How to Run

If you want to run this API on your own machine:

1) **Clone the repository**
   ```bash
   git clone [https://github.com/Ankush1505/Bookstore-FastApi-Project.git](https://github.com/Ankush1505/Bookstore-FastApi-Project.git)
   
   cd Bookstore-FastApi-Project

2) python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

3) pip install -r requirements.txt

4) Set up Environment Variables: 
     CREATE a .env file in the root directory and add your database credentials:
            DATABASE_HOSTNAME=localhost
            DATABASE_PORT=5432
            DATABASE_PASSWORD=your_password
            DATABASE_NAME=bookstore
            DATABASE_USERNAME=postgres
            SECRET_KEY=your_secret_key
            ALGORITHM=HS256
            ACCESS_TOKEN_EXPIRE_MINUTES=30
   
6) Run the Server: uvicorn main:app --reload





   
