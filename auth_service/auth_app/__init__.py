from flask import Flask
from . import routes
from flask_smorest import Api

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object("config")
    # app.register_blueprint(routes.bp_auth)

    app.config['API_TITLE'] = 'Auth API'
    app.config['API_VERSION'] = 'v1'
    app.config['OPENAPI_VERSION'] = '3.0.3'
    app.config['OPENAPI_URL_PREFIX'] = '/docs'
    app.config['OPENAPI_SWAGGER_UI_PATH'] = '/swagger-ui'
    app.config['OPENAPI_SWAGGER_UI_URL'] = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'

    @app.route('/auth')
    def hello():
        return "Hello from auth_service"

    api = Api(app)
    api.register_blueprint(routes.bp_auth)

    return app