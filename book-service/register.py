import requests

response = requests.post(
    "http://localhost:5000/register",
    json={
        "name": "book-service",
        "url": "http://localhost:5002"
    }
)

print(response.json())
python book-service/register.py
