# Sample Azure Function App (Python)

A sample Python Azure Function app with HTTP triggers for `/users`, `/api`, and `/places`.

## Endpoints

| Route  | Description                     |
|--------|---------------------------------|
| `/users` | Returns a list of sample users |
| `/api`   | Catch-all endpoint (accepts any path under /api) |
| `/places` | Returns random cities (optional `?count=N` query param, default 5) |

## Prerequisites

- Python 3.9, 3.10, or 3.11
- [Azure Functions Core Tools](https://docs.microsoft.com/azure/azure-functions/functions-run-local) v4

## Setup & Run

```bash
# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run locally
func start
```

The app will run at `http://localhost:7071`.

## Example requests

```bash
# List users
curl http://localhost:7071/users

# API catch-all (e.g. /api or /api/foo/bar)
curl http://localhost:7071/api
curl http://localhost:7071/api/items/123

# List random cities (default 5)
curl http://localhost:7071/places

# List 10 random cities
curl "http://localhost:7071/places?count=10"
```
