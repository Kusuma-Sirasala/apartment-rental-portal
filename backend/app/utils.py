# You can add helper functions here
def format_apartment(apartment):
    return {
        "id": apartment.id,
        "tower_name": apartment.tower_name,
        "unit_number": apartment.unit_number,
        "bedrooms": apartment.bedrooms,
        "rent": apartment.rent,
        "amenities": apartment.amenities,
        "is_available": apartment.is_available
    }

