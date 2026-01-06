from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ------------------ MOCK DATA ------------------
users = []
apartments = [
    {
        "id": 1,
        "name": "Green View Apartments",
        "bhk": "2 BHK",
        "rent": 12000,
        "image": "https://via.placeholder.com/300"
    },
    {
        "id": 2,
        "name": "Skyline Residency",
        "bhk": "3 BHK",
        "rent": 18000,
        "image": "https://via.placeholder.com/300"
    }
]

# ------------------ ROUTES ------------------

@app.route("/")
def home():
    return "Backend running"

@app.route("/api/register", methods=["POST"])
def register():
    data = request.json
    users.append(data)
    return jsonify({"status": "success", "message": "User registered"})

@app.route("/api/login", methods=["POST"])
def login():
    data = request.json
    return jsonify({"status": "success", "message": "Login API working"})

@app.route("/api/apartments", methods=["GET"])
def get_apartments():
    return jsonify(apartments)

# ------------------ RUN ------------------
if __name__ == "__main__":
    app.run(debug=True)