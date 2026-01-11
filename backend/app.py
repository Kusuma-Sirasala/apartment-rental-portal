from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Backend Running"

@app.route("/api/register", methods=["POST"])
def register():
    return jsonify({
        "status": "success",
        "message": "User registered successfully"
    })

@app.route("/api/login", methods=["POST"])
def login():
    return jsonify({
        "status": "success",
        "message": "Login successful"
    })
@app.route("/api/book", methods=["POST"])
def book_apartment():
    return jsonify({
        "status": "success",
        "message": "Apartment booked successfully ! Our team will contact you soon."
    })
@app.route("/api/apartments", methods=["GET"])
def apartments():
    return jsonify([
        {
            "id": 1,
            "name": "Green View Apartments",
            "bhk": "2 BHK",
            "rent": 12000,
            "image": "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2"
        },
        {
            "id": 2,
            "name": "Skyline Residency",
            "bhk": "3 BHK",
            "rent": 18000,
            "image": "https://images.unsplash.com/photo-1502672260266-1c1ef2d93688"
        },
        {
            "id": 3,
            "name": "Lake View Towers",
            "bhk": "1 BHK",
            "rent": 9000,
            "image": "https://images.unsplash.com/photo-1523217582562-09d0def993a6"
        },
        {
            "id": 4,
            "name": "Sunshine Heights",
            "bhk": "2 BHK",
            "rent": 14000,
            "image": "https://images.unsplash.com/photo-1572120360610-d971b9d7767c"
        },
        {
            "id": 5,
            "name": "Royal Residency",
            "bhk": "3 BHK",
            "rent": 22000,
            "image": "https://images.unsplash.com/photo-1568605114967-8130f3a36994"
        }
    ])

if __name__ == "__main__":
    app.run(debug=True)