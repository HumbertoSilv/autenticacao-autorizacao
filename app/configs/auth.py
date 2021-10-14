from app.models.user_model import Usermodel
from flask_httpauth import HTTPTokenAuth

auth = HTTPTokenAuth(scheme="Bearer")


@auth.verify_token
def verify_token(token):
    user = Usermodel.query.filter_by(api_key=token).first()
    return user
