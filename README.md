# FastAPISample

This project is a sample FastAPI application that demonstrates how to create and manage users and customers using FastAPI, SQLAlchemy, and SQLite.

## Project Structure

- `app/`: Contains the main application code
  - `database.py`: Database configuration and session management
  - `models.py`: SQLAlchemy models for the application
  - `routes/`: API route definitions
    - `customers.py`: API routes for managing customers
    - `users.py`: API routes for managing users
  - `schema.py`: Pydantic schemas for request and response validation
  - `services/`: Service layer for business logic
    - `customers.py`: Customer service logic
    - `users.py`: User service logic
- `main.py`: Entry point for the FastAPI application
- `requirements.txt`: List of dependencies for the project
- `Dockerfile`: Docker configuration for the application
- `docker-compose.yml`: Docker Compose configuration for the application

## Prerequisites

- Python 3.9 or higher
- Docker (optional, for running the application in a container)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/callingmahendra/FastAPISample.git
cd FastAPISample
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application Locally

1. Start the FastAPI application:

```bash
fastapi dev main.py
```

2. Open your browser and navigate to `http://127.0.0.1:8000` to access the application.

3. You can also access the automatically generated API documentation at `http://127.0.0.1:8000/docs` (Swagger UI) and `http://127.0.0.1:8000/redoc` (ReDoc).

## Running the Application with Docker

1. Build the Docker image:

```bash
docker build -t fastapi-sample .
```

2. Start the application using Docker Compose:

```bash
docker-compose up
```

3. Open your browser and navigate to `http://127.0.0.1:8000` to access the application.

4. You can also access the automatically generated API documentation at `http://127.0.0.1:8000/docs` (Swagger UI) and `http://127.0.0.1:8000/redoc` (ReDoc).

## Running Tests with Pytest

1. Install pytest if you haven't already:

```bash
pip install pytest
```

2. Run the tests:

```bash
pytest
```

## License

This project is licensed under the terms of the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.
