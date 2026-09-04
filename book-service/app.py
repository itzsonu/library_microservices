from flask import Flask

app = Flask(__name__)

books = {
    "1": {
        "id": "1",
        "title": "Python Programming",
        "author": "Guido van Rossum"
    },
    "2": {
        "id": "2",
        "title": "Clean Code",
        "author": "Robert C. Martin"
    },
    "3": {
        "id": "3",
        "title": "The Pragmatic Programmer",
        "author": "Andrew Hunt"
    }
}


@app.route("/books/<book_id>")
def get_book(book_id):

    book = books.get(book_id)

    if not book:
        return {"error": "Book not found"}, 404

    return book


if __name__ == "__main__":
    app.run(port=5002)