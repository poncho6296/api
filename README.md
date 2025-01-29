# Space Rescue API

This is a FastAPI application that simulates a space rescue system with three endpoints:

## Endpoints

- `GET /status`: Returns a random damaged system
- `GET /repair-bay`: Shows HTML page with repair code for the current system
- `POST /teapot`: Returns 418 I'm a teapot status code

## Local Development

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
uvicorn main:app --reload
```

## Deployment

This application is configured for deployment on Azure App Service.