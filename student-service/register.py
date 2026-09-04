import requests

response = requests.post(
    "http://localhost:5000/register",
    json={
        "name": "student-service",
        "url": "http://localhost:5001"
    }
)

print(response.json())
python student-service/register.py
