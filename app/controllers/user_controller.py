import sqlalchemy
from app.models.user_model import Usermodel
from flask import current_app, jsonify, request
from flask_jwt_extended import (
    create_access_token, jwt_required, get_jwt_identity
)


def create_user():
    data = request.json
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

    access_token = create_access_token(identity=exists_user)

    return jsonify({"access_token": access_token}), 200


@jwt_required()
def get_user():
    current_user = get_jwt_identity()
    return jsonify(current_user), 200


@jwt_required()
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


@jwt_required()
def delete_user():
    user = get_jwt_identity()
    found_user = Usermodel.query.filter_by(email=user["email"]).first()

    current_app.db.session.delete(found_user)
    current_app.db.session.commit()
    print(user, found_user)

    return {"msg": f"User {user['name']} has been deleted."}, 200
