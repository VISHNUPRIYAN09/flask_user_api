
Flask User API

A simple RESTful API built with Flask to manage users. Supports basic CRUD operations: Create, Read, Update, and Delete users.

Features

- Get all users  
- Get user by ID  
- Create new user  
- Update existing user  
- Delete user  

Technologies Used

- Python  
- Flask  

How to Run

1. Clone the repo  
2. Install dependencies:  
   pip install flask  
3. Run the app:  
   python app.py  
4. Access the API at http://127.0.0.1:5000

API Endpoints

| Method | Endpoint         | Description        |
|--------|------------------|--------------------|
| GET    | /users           | Get all users      |
| GET    | /users/&lt;id&gt; | Get user by ID     |
| POST   | /users           | Create a new user  |
| PUT    | /users/&lt;id&gt; | Update user by ID  |
| DELETE | /users/&lt;id&gt; | Delete user by ID  |

