from server.controllers.guest_controller import guest_bp
from server.controllers.episode_controller import episode_bp
from server.controllers.appearance_controller import appearance_bp
from server.controllers.auth_controller import auth_bp

all_blueprints = [
    guest_bp,
    episode_bp,
    appearance_bp,
    auth_bp
]
