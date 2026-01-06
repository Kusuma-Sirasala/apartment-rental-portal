from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app import db
from models import Unit, Amenity, Booking
from app.utils import admin_required

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")


# -------------------- UNITS --------------------

@admin_bp.route("/units", methods=["POST"])
@jwt_required()
def add_unit():
    if not admin_required():
        return jsonify(msg="Access denied. Admin only."), 403

    data = request.json
    unit = Unit(
        tower=data["tower"],
        flat_no=data["flat_no"],
        rent=data["rent"],
        status="AVAILABLE"
    )

    db.session.add(unit)
    db.session.commit()
    return jsonify(msg="Unit added successfully")


@admin_bp.route("/units", methods=["GET"])
@jwt_required()
def get_units():
    if not admin_required():
        return jsonify(msg="Access denied. Admin only."), 403

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


# -------------------- AMENITIES --------------------

@admin_bp.route("/amenities", methods=["POST"])
@jwt_required()
def add_amenity():
    if not admin_required():
        return jsonify(msg="Access denied. Admin only."), 403

    data = request.json
    amenity = Amenity(name=data["name"])

    db.session.add(amenity)
    db.session.commit()
    return jsonify(msg="Amenity added successfully")


@admin_bp.route("/amenities", methods=["GET"])
@jwt_required()
def get_amenities():
    if not admin_required():
        return jsonify(msg="Access denied. Admin only."), 403

    amenities = Amenity.query.all()
    return jsonify([
        {
            "id": a.id,
            "name": a.name
        } for a in amenities
    ])


# -------------------- BOOKINGS --------------------

@admin_bp.route("/bookings", methods=["GET"])
@jwt_required()
def get_all_bookings():
    if not admin_required():
        return jsonify(msg="Access denied. Admin only."), 403

    bookings = Booking.query.all()
    return jsonify([
        {
            "id": b.id,
            "user_id": b.user_id,
            "unit_id": b.unit_id,
            "status": b.status
        } for b in bookings
    ])


@admin_bp.route("/bookings/<int:booking_id>/approve", methods=["PUT"])
@jwt_required()
def approve_booking(booking_id):
    if not admin_required():
        return jsonify(msg="Access denied. Admin only."), 403

    booking = Booking.query.get(booking_id)
    if not booking:
        return jsonify(msg="Booking not found"), 404

    booking.status = "APPROVED"
    db.session.commit()

    return jsonify(msg="Booking approved")


@admin_bp.route("/bookings/<int:booking_id>/reject", methods=["PUT"])
@jwt_required()
def reject_booking(booking_id):
    if not admin_required():
        return jsonify(msg="Access denied. Admin only."), 403

    booking = Booking.query.get(booking_id)
    if not booking:
        return jsonify(msg="Booking not found"), 404

    booking.status = "REJECTED"
    db.session.commit()

    return jsonify(msg="Booking rejected")
