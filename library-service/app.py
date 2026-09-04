from flask import Flask
import requests

app = Flask(__name__)

REGISTRY_URL = "http://localhost:5000"

def discover(service_name):
    response = requests.get(
        f"{REGISTRY_URL}/discover/{service_name}"
    )
    if response.status_code != 200:
        return None
    return response.json()["url"]

@app.route("/borrow/<student_id>/<book_id>")
def borrow_book(student_id, book_id):
student_service = discover("student-service")
    if not student_service:
        return {"error": "Student Service not available"}, 503

    student_response = requests.get(
        f"{student_service}/students/{student_id}"
    )
    if student_response.status_code != 200:
        return {"error": "Student not found"}, 404
    student = student_response.json()

    book_service = discover("book-service")
    if not book_service:
        return {"error": "Book Service not available"}, 503

    book_response = requests.get(
        f"{book_service}/books/{book_id}"
    )
    if book_response.status_code != 200:
        return {"error": "Book not found"}, 404
    book = book_response.json()

    return {
        "message": "Book borrowed successfully",
        "student": student,
        "book": book
    }

app.run(port=5003)
