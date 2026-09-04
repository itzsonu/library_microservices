from flask import Flask

app = Flask(__name__)

students = {
    "101": {
        "id": 101,
        "name": "John"
    },
    "102": {
        "id": 102,
        "name": "Alice"
    }
}


@app.route("/students/<student_id>")
def get_student(student_id):

    student = students.get(student_id)

    if not student:
        return {
            "error": "Student not found"
        }, 404

    return student


if __name__ == "__main__":
    app.run(port=5001)