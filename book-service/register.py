import requests

REGISTRY_URL = "http://localhost:5000"

data = {
    "name": "book-service",
    "url": "http://localhost:5002"
}

response = requests.post(
    f"{REGISTRY_URL}/register",
    json=data
)

print(response.json())