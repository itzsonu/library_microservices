from flask import Flask
import requests

app = Flask(__name__)

REGISTRY_URL = "http://localhost:5000"


def discover(service_name):
    try:
        response = requests.get(
            f"{REGISTRY_URL}/discover/{service_name}",
            timeout=5
        )

        if response.status_code != 200:
            return None

        return response.json()["url"]

    except requests.RequestException:
        return None


@app.route("/borrow/<student_id>/<book_id>")
def borrow_book(student_id, book_id):

    # Discover Student Service
    student_service = discover("student-service")

    if not student_service:
        return {"error": "Student Service unavailable"}, 503

    # Get student
    try:
        student_response = requests.get(
            f"{student_service}/students/{student_id}",
            timeout=5
        )
    except requests.RequestException:
        return {"error": "Student Service unavailable"}, 503

    if student_response.status_code != 200:
        return {"error": "Student not found"}, 404

    student = student_response.json()

    # Discover Book Service
    book_service = discover("book-service")

    if not book_service:
        return {"error": "Book Service unavailable"}, 503

    # Get book
    try:
        book_response = requests.get(
            f"{book_service}/books/{book_id}",
            timeout=5
        )
    except requests.RequestException:
        return {"error": "Book Service unavailable"}, 503

    if book_response.status_code != 200:
        return {"error": "Book not found"}, 404

    book = book_response.json()

    return {
        "message": "Book borrowed successfully",
        "student": student,
        "book": book
    }


if __name__ == "__main__":
    app.run(port=5003)