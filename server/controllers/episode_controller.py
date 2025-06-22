from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from server.models.episode import Episode
from server.app import db

episode_bp = Blueprint("episodes", __name__, url_prefix="/episodes")

@episode_bp.route("/", methods=["GET"])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([{"id": e.id, "date": e.date, "number": e.number} for e in episodes])

@episode_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_episode(id):
    episode = Episode.query.get_or_404(id)
    db.session.delete(episode)
    db.session.commit()
    return {"message": "Deleted"}, 204
