from flask import Flask
from .routes import bp_menu
from flask_smorest import Api

from .db import db
from flask_migrate import Migrate
from .models import MenuItem

menu_db = {}

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object("config")
    app.config['menu_db'] = menu_db
    # app.register_blueprint(bp_menu)

    app.config['API_TITLE'] = 'Menu API'
    app.config['API_VERSION'] = 'v1'
    app.config['OPENAPI_VERSION'] = '3.0.3'
    app.config['OPENAPI_URL_PREFIX'] = '/docs'
    app.config['OPENAPI_SWAGGER_UI_PATH'] = '/swagger-ui'
    app.config['OPENAPI_SWAGGER_UI_URL'] = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'

    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Menuservice123@menu-service-db.c8nciwy02l1a.us-east-1.rds.amazonaws.com:5432/menu_service_db"

    db.init_app(app)

    migrate = Migrate(app, db)

    api = Api(app)
    api.register_blueprint(bp_menu)

    return app