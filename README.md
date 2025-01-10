# My Flask Application

This project is a Flask-based application deployed using a robust CI/CD pipeline. The application and its infrastructure are managed with Docker and Kubernetes. The pipeline is configured with GitHub Actions to automate testing, building, and deploying the application.

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

The `cd.yaml` workflow automates the deployment of the Flask application to a Kubernetes cluster.

- **Trigger**:
  - Runs on push to the `main` branch or manually via `workflow_dispatch`.
- **Steps**:
  1. **Code Checkout**: Fetch the latest code.
  2. **Build Docker Image**: Build the Docker image for the Flask application.
  3. **Vulnerability Scan**: Scan the Docker image for vulnerabilities using Trivy.
  4. **Push to Registry**: Push the Docker image to a specified container registry.
  5. **Database Migration**: Apply SQL migrations (if required).


**Workflow File:** [cd.yaml](.github/workflows/cd.yaml)

## Docker Image

The application is containerized using the following `Dockerfile`:

```dockerfile
# Use an official Python runtime
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY app/ ./app

# Expose the Flask port
EXPOSE 5000

# Run the application
CMD ["python", "app/main.py"]
```

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
```

To install the dependencies:

```bash
pip install -r requirements.txt
```


This project is a demonstration of a complete CI/CD pipeline using modern tools like GitHub Actions and Docker. It serves as a template for deploying Flask applications in production-ready environments.

