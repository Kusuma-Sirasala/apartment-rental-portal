from flask import Blueprint, request, jsonify

api = Blueprint("api", __name__)

# ---------------- REGISTER ----------------
@api.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    if not data:
        return jsonify({"status": "error", "message": "No data received"}), 400

    return jsonify({
        "status": "success",
        "message": "User registered successfully"
    }), 201


# ---------------- LOGIN ----------------
@api.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data:
        return jsonify({"status": "error", "message": "No data received"}), 400

    return jsonify({
        "status": "success",
        "message": "User logged in successfully"
    }), 200


# ---------------- APARTMENTS ----------------
@api.route("/apartments", methods=["GET"])
def apartments():
    apartments_list = [
        {
            "id": 1,
            "name": "Cozy Studio",
            "bhk": "1 BHK",
            "rent": 8000,
            "image": "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2"
        },
        {
            "id": 2,
            "name": "Sunny Apartments",
            "bhk": "2 BHK",
            "rent": 12000,
            "image": "https://images.unsplash.com/photo-1522708323590-d24dbb6b0267"
        },
        {
            "id": 3,
            "name": "Honey Living",
            "bhk": "3 BHK",
            "rent": 18000,
            "image": "https://images.unsplash.com/photo-1512917774080-9991f1c4c750"
        }
    ]

    return jsonify(apartments_list), 200


# ---------------- BOOKING ----------------
@api.route("/book", methods=["POST"])
def book_apartment():
    data = request.get_json()

    if not data or "apartment" not in data:
        return jsonify({"message": "Apartment name required"}), 400

    return jsonify({
        "status": "success",
        "message": f"Booking successful for {data['apartment']}. Our contact team will call you shortly."
    }), 200
