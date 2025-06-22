from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from server.models.appearance import Appearance
from server.app import db

appearance_bp = Blueprint("appearances", __name__, url_prefix="/appearances")

@appearance_bp.route("/", methods=["POST"])
@jwt_required()
def create_appearance():
    data = request.get_json()
    new_appearance = Appearance(
        rating=data["rating"],
        guest_id=data["guest_id"],
        episode_id=data["episode_id"]
    )
    db.session.add(new_appearance)
    db.session.commit()
    return jsonify({"message": "Appearance created"}), 201
