from flask import Flask
from .routes import bp_order
from flask_smorest import Api

from .db import db
from .models import Order, OrderItem
from flask_migrate import Migrate

inventory_db = {'pizza': 10, 'burger': 5, 'burrito': 20}
orders_db = {}
order_id_int = 100

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config')
    app.config['inventory_db'] = inventory_db
    app.config['orders_db'] = orders_db
    app.config['order_id_int'] = order_id_int

    # app.register_blueprint(bp_order)

    app.config['API_TITLE'] = 'Order API'
    app.config['API_VERSION'] = 'v1'
    app.config['OPENAPI_VERSION'] = '3.0.3'
    app.config['OPENAPI_URL_PREFIX'] = '/docs'
    app.config['OPENAPI_SWAGGER_UI_PATH'] = '/swagger-ui'
    app.config['OPENAPI_SWAGGER_UI_URL'] = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'

    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Orderservice123@order-service-db.c8nciwy02l1a.us-east-1.rds.amazonaws.com:5432/order_service_db"

    db.init_app(app)

    migrate = Migrate(app, db)

    api = Api(app)
    api.register_blueprint(bp_order)

    return app