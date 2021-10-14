from flask import request, jsonify, current_app
from app.models.user_model import Usermodel
from secrets import token_urlsafe
from app.configs.auth import auth
import sqlalchemy


def create_user():
    data = request.json
    data["api_key"] = token_urlsafe(16)
    password_to_hash = data.pop("password")

    new_user = Usermodel(**data)
    new_user.password = password_to_hash

    current_app.db.session.add(new_user)
    current_app.db.session.commit()

    return jsonify(new_user), 201


def login_user():
    data = request.json

    exists_user = Usermodel.query.filter_by(email=data["email"]).first()
    if not exists_user:
        return {"msg": "User not found."}, 404

    check_password = exists_user.verify_password(data["password"])
    if not check_password:
        return {"msg": "Incorrect password."}, 401

    return jsonify({"api_key": exists_user.api_key}), 200


@auth.login_required
def get_user():
    return jsonify(auth.current_user())


@auth.login_required
def update_user():
    data = request.json
    if len(data) != 4:
        return {"msg": "Incorrect number of fields"}, 400

    try:
        user_update = Usermodel.query.filter_by(email=data["email"]).first()
        password = data.pop("password")
        user_update.password = password

        Usermodel.query.filter_by(email=data["email"]).update(data)
        current_app.db.session.commit()
    except sqlalchemy.exc.InvalidRequestError:
        return {"msg": "Invalid fields."}, 400

    return jsonify(user_update), 200


@auth.login_required
def delete_user():
    current_app.db.session.delete(auth.current_user())
    current_app.db.session.commit()

    return {"msg": "User John has been deleted."}, 200
