# FastAPI CRUD API

This is a simple FastAPI application that provides CRUD (Create, Read, Update, Delete) operations for a user model.

## Features

- Create User: Add a new user to the database.
- Read Users: Retrieve a list of all users in the database.
- Read User: Retrieve details of a specific user using their unique identifier.
- Update User: Modify the details of an existing user.
- Delete User: Remove a user from the database.

## Installation

To install the FastAPI CRUD API, follow these steps:

1. Clone the repository:
   bash
   git clone https://github.com/your_username/fastapi-crud-api.git
2. Install the dependencies:
   bash
   pip install -r requirements.txt

## Usage

To run the FastAPI application, follow these steps:

1. Open a terminal window and navigate to the directory where you cloned the repository.
2. Run the following command:
   bash
   uvicorn your_file_name:app --reload
   Replace your_file_name with the actual name of the Python file containing your FastAPI application.

3. Open your browser and navigate to:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc UI: http://127.0.0.1:8000/redoc

4. Explore and interact with the API using the provided documentation.

## API Endpoints

The FastAPI CRUD API provides the following endpoints:

- GET /api/v1/users : Retrieve a list of all users.
- GET /api/v1/users/{user_id} : Retrieve details of a specific user.
- POST /api/v1/users : Create a new user.
- PUT /api/v1/users/{user_id} : Update details of an existing user.
- DELETE /api/v1/users/{user_id} : Delete a user from the database.

## Dependencies

The FastAPI CRUD API depends on the following libraries:

- FastAPI
- uvicorn

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
