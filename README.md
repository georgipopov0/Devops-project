# My Flask Application

This project is a Flask-based application deployed using a robust CI/CD pipeline. The application and its infrastructure are managed with Docker and SQLAlchemy-based database migrations. The pipeline is configured with GitHub Actions to automate testing, building, and deploying the application.

## Project Structure

```plaintext
my-flask-app/
├── app/               # Application source code
├── tests/             # Unit tests
├── .github/
│   └── workflows/     # CI/CD workflows
│       ├── ci.yaml    # Continuous Integration workflow
│       └── cd.yaml    # Continuous Deployment workflow
├── Dockerfile         # Docker image definition
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
```

## CI/CD Pipeline

The project leverages GitHub Actions for Continuous Integration (CI) and Continuous Deployment (CD). Below is a breakdown of the workflows:

### Continuous Integration (CI)

The `ci.yaml` workflow ensures code quality and reliability by performing the following steps:

- **Trigger**:
  - Runs on every push or pull request to `main`, `dev`, or `feature/*` branches.
- **Steps**:
  1. **Code Checkout**: Fetch the latest code.
  2. **Python Setup**: Install Python 3.9 and dependencies listed in `requirements.txt`.
  3. **Linting**: Use `flake8` to enforce coding standards.
  4. **Code Formatting Check**: Verify code formatting using `black`.
  5. **Static Analysis**: Run security checks with `bandit`.
  6. **Testing**: Execute unit tests with `pytest` and generate code coverage reports.

**Workflow File:** [ci.yaml](.github/workflows/ci.yaml)

### Continuous Deployment (CD)

The `cd.yaml` workflow automates the deployment of the Flask application, including applying database migrations.

- **Trigger**:
  - Runs on push to the `main` branch or manually via `workflow_dispatch`.
- **Steps**:
  1. **Code Checkout**: Fetch the latest code.
  2. **Python Setup**: Install Python 3.9 and dependencies.
  3. **Database Migration**: Apply database migrations using Flask-Migrate.

**Workflow File:** [cd.yaml](.github/workflows/cd.yaml)


### Building the Docker Image

To build the Docker image locally:

```bash
docker build -t my-flask-app:latest .
```

### Running the Docker Container

To run the container locally:

```bash
docker run -p 5000:5000 my-flask-app:latest
```

## Python Requirements

The application dependencies are managed in `requirements.txt`:

```plaintext
Flask
pytest
pytest-cov
flake8
black
bandit
SQLAlchemy
Flask-Migrate
```

To install the dependencies:

```bash
pip install -r requirements.txt
```

## Database and Migrations

This project uses **SQLAlchemy** for ORM and **Flask-Migrate** for database migrations.

### Setting up the Database

By default, the application uses SQLite as the database, configured in `app/main.py`:

```python
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
```

Update the `SQLALCHEMY_DATABASE_URI` if using another database (e.g., PostgreSQL or MySQL).

### Running Migrations Locally

1. Initialize the migration environment:

   ```bash
   flask db init
   ```

2. Create a migration script based on changes to models:

   ```bash
   flask db migrate -m "Initial migration"
   ```

3. Apply migrations to update the database schema:

   ```bash
   flask db upgrade
   ```

### Running Migrations in CI/CD

The CD workflow includes a step to apply migrations:

```yaml
- name: Apply Database Migrations
  env:
    FLASK_APP: app.main.py
  run: |
    flask db upgrade
```

## Running Locally

To run the application locally:

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Start the Flask application:

   ```bash
   python app/main.py
   ```

3. Open your browser and navigate to `http://localhost:5000`.

## Unit Testing

The project includes unit tests to verify application functionality.

### Running Tests

To run tests locally:

```bash
pytest tests/
```

### Test Example

An example test is provided in `tests/test_app.py`:

```python
from app.main import app

def test_hello():
    test_client = app.test_client()
    response = test_client.get("/")
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, DevOps!"}
```

This project is a demonstration of a complete CI/CD pipeline using modern tools like GitHub Actions, Docker, and Flask-Migrate. It serves as a template for deploying Flask applications with database integration in production-ready environments.

