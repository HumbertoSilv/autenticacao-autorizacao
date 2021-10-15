from flask import Flask
from app.configs import env_configs, database, migrate, jwt
from app.blueprints import user_blueprint


def create_app(app: Flask):
    app = Flask(__name__)
    env_configs.init_app(app)
    database.init_app(app)
    migrate.init_app(app)
    jwt.init_app(app)
    app.register_blueprint(user_blueprint.bp)

    return app
