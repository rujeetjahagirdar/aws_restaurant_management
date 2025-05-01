from flask import Flask
from . import routes
from flask_smorest import Api
from .db import db
from .models import User
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object("config")
    # app.register_blueprint(routes.bp_user)
    # app.register_blueprint(routes.bp_users)

    app.config['API_TITLE'] = 'User API'
    app.config['API_VERSION'] = 'v1'
    app.config['OPENAPI_VERSION'] = '3.0.3'
    app.config['OPENAPI_URL_PREFIX'] = '/docs'
    app.config['OPENAPI_SWAGGER_UI_PATH'] = '/swagger-ui'
    app.config['OPENAPI_SWAGGER_UI_URL'] = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'

    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Userservice123@user-service-db.c8nciwy02l1a.us-east-1.rds.amazonaws.com:5432/user_service_db"

    db.init_app(app)

    migrate = Migrate(app, db)


    @app.route('/user')
    def hello():
        return "Hello from user_service"

    api = Api(app)
    api.register_blueprint(routes.bp_user)
    api.register_blueprint(routes.bp_users)


    return app