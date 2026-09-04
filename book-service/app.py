from flask import Flask

app = Flask(__name__)

books = {
    "1": {"id": 1, "title": "Python Programming"},
    "2": {"id": 2, "title": "Microservices Basics"},
    "3": {"id": 3, "title": "Kubernetes for Beginners"}
}

@app.route("/books/<book_id>")
def get_book(book_id):
    book = books.get(book_id)
    if not book:
        return {"error": "Book not found"}, 404
    return book

app.run(port=5002)
python book-service/app.py
http://localhost:5002/books/1
