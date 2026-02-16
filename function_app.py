"""
Sample Azure Function App with HTTP Triggers
Routes: /users, /api, /places
"""

import json
import random
import azure.functions as func

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

# Sample data
SAMPLE_USERS = [
    {"id": 1, "name": "Alice Johnson", "email": "alice@example.com"},
    {"id": 2, "name": "Bob Smith", "email": "bob@example.com"},
    {"id": 3, "name": "Carol Williams", "email": "carol@example.com"},
    {"id": 4, "name": "David Brown", "email": "david@example.com"},
    {"id": 5, "name": "Eva Davis", "email": "eva@example.com"},
    {"id": 7, "name": "Grace Wilson", "email": "grace@example.com"},
    {"id": 8, "name": "Henry Davis", "email": "henry@example.com"},
    {"id": 9, "name": "Ivy Taylor", "email": "ivy@example.com"},
    {"id": 10, "name": "Jack Johnson", "email": "jack@example.com"},
]

SAMPLE_CITIES = [
    "Tokyo", "New York", "London", "Paris", "Sydney",
    "Berlin", "Singapore", "Dubai", "Toronto", "Mumbai",
    "São Paulo", "Mexico City", "Seoul", "Amsterdam", "Rome",
    "San Francisco", "Chicago", "Los Angeles", "Miami", "Madrid",
    "Berlin", "Singapore", "Dubai", "Toronto", "Mumbai",
    "São Paulo", "Mexico City", "Seoul", "Amsterdam", "Rome",
    "San Francisco", "Chicago", "Los Angeles", "Miami", "Madrid",
    "Berlin", "Singapore", "Dubai", "Toronto", "Mumbai",
    "São Paulo", "Mexico City", "Seoul", "Amsterdam", "Rome",
    "San Francisco", "Chicago", "Los Angeles", "Miami", "Madrid",
    "Berlin", "Singapore", "Dubai", "Toronto", "Mumbai",
    "São Paulo", "Mexico City", "Seoul", "Amsterdam", "Rome",
]


@app.function_name(name="users")
@app.route(route="users", methods=["GET"])
def users(req: func.HttpRequest) -> func.HttpResponse:
    """List down users."""
    return func.HttpResponse(
        body=json.dumps({"users": SAMPLE_USERS}, indent=2),
        mimetype="application/json",
        status_code=200,
    )


@app.function_name(name="api")
@app.route(route="api/{*restOfPath}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
def api(req: func.HttpRequest) -> func.HttpResponse:
    """Catch-all API endpoint - handles any request to /api."""
    path = req.route_params.get("restOfPath", "")
    method = req.method

    payload = {
        "message": "API endpoint reached",
        "method": method,
        "path": path or "(root)",
        "query_params": dict(req.params),
    }

    return func.HttpResponse(
        body=json.dumps(payload, indent=2),
        mimetype="application/json",
        status_code=200,
    )


@app.function_name(name="places")
@app.route(route="places", methods=["GET"])
def places(req: func.HttpRequest) -> func.HttpResponse:
    """List down random cities."""
    count = int(req.params.get("count", 5))
    count = min(max(count, 1), len(SAMPLE_CITIES))
    selected = random.sample(SAMPLE_CITIES, count)

    return func.HttpResponse(
        body=json.dumps({"cities": selected}, indent=2),
        mimetype="application/json",
        status_code=200,
    )
