from flask import Flask

from app.blueprints import user_blueprint
from app.configs import database, env_configs, jwt, migrate


def create_app(app: Flask):
    app = Flask(__name__)
    env_configs.init_app(app)
    database.init_app(app)
    migrate.init_app(app)
    jwt.init_app(app)
    app.register_blueprint(user_blueprint.bp)

    return app
