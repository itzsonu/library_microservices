from flask import Flask, request

app = Flask(__name__)

services = {}


@app.route("/register", methods=["POST"])
def register_service():
    data = request.json

    name = data["name"]
    url = data["url"]

    services[name] = url

    return {
        "message": "Service registered successfully",
        "service": name,
        "url": url
    }


@app.route("/discover/<name>")
def discover_service(name):
    if name not in services:
        return {"error": "Service not found"}, 404

    return {
        "service": name,
        "url": services[name]
    }


@app.route("/services")
def get_services():
    return services


if __name__ == "__main__":
    app.run(port=5000)