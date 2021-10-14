from flask import Blueprint
from app.controllers.user_controller import (
    create_user, login_user, get_user, update_user, delete_user
)

bp = Blueprint("user_bp", __name__, url_prefix="/api")

bp.post("/signup")(create_user)
bp.post("/signin")(login_user)
bp.get("")(get_user)
bp.put("")(update_user)
bp.delete("")(delete_user)
