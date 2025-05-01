from flask import Flask
from .routes import bp_availability, book
from flask_smorest import Api

from .db import db
from .models import Table, Booking
from flask_migrate import Migrate

tables_db = {'T01': {'capacity': 4, 'booking_time': None}, 'T02': {'capacity': 3, 'booking_time': None},
             'T03': {'capacity': 4, 'booking_time': None}, 'T04': {'capacity': 2, 'booking_time': None}}

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object("config")
    app.config['tables_db'] = tables_db

    app.config['API_TITLE'] = 'Booking API'
    app.config['API_VERSION'] = 'v1'
    app.config['OPENAPI_VERSION'] = '3.0.3'
    app.config['OPENAPI_URL_PREFIX'] = '/docs'
    app.config['OPENAPI_SWAGGER_UI_PATH'] = '/swagger-ui'
    app.config['OPENAPI_SWAGGER_UI_URL'] = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'

    app.config[
        'SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Bookingservice123@booking-service-db.c8nciwy02l1a.us-east-1.rds.amazonaws.com:5432/booking_service_db"

    db.init_app(app)

    migrate = Migrate(app, db)

    api = Api(app)
    api.register_blueprint(bp_availability)

    # @app.route('/check_availability')
    # def hello():
    #     return "Hello from check_availability service"

    return app