from flask import Blueprint, request
from . import utils
from flask_smorest import Blueprint

bp_auth = Blueprint('auth', __name__, url_prefix='/auth')

@bp_auth.route('/signup', methods=["GET", "POST"])
def signup():
    if(request.method=='GET'):
        result = utils.cognito_get_users()
        return result['Users']
    elif(request.method=='POST'):
        data = request.json
        return utils.cognito_signup(data)



@bp_auth.route('/login', methods=["GET", "POST"])
def login():
    if(request.method=='POST'):
        data = request.json
        return utils.cognito_login(data)
    elif(request.method=='GET'):
        return "Hello from auth/login API"


@bp_auth.route('/verify_token', methods=["GET", "POST"])
def verify_token():
    if(request.method=='GET'):
        token = request.headers.get("Authorization")
        return utils.cognito_verify_token(token)