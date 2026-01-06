from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import Unit, Booking
from app import db

booking_bp = Blueprint("booking", __name__)

@booking_bp.route("/units")
@jwt_required()
def get_units():
    units = Unit.query.all()
    return jsonify([
        {
            "id": u.id,
            "tower": u.tower,
            "flat_no": u.flat_no,
            "rent": u.rent,
            "status": u.status
        } for u in units
    ])
