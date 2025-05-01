from flask import request
from .auth import required_auth
from .utils import get_user_details, update_user_details, get_users, create_user
from flask_smorest import Blueprint
from .schemas import UserGetResponseSchema, UserGetRequestSchema, UserPutRequestSchema, UserPutResponseSchema, \
    UsersGetRequestSchema, UsersGetResponseSchema, UsersPostRequestSchema, UsersPostResponseSchema

bp_user = Blueprint('user', __name__, url_prefix='/user', description= "Endpoint for User profile")
bp_users = Blueprint('users', __name__, url_prefix='/users', description= "Endpoint for All User profiles")

@bp_user.route('/<int:user_id>', methods=['GET'])
# we are using GET request with path parameter, so we do not need @bp.arguments
@bp_user.response(200, UserGetResponseSchema)
# @required_auth
def user(user_id):
    return get_user_details(user_id)

@bp_user.route('/<int:user_id>', methods=['PUT'])
@bp_user.arguments(UserPutRequestSchema, location='json')
@bp_user.response(200, UserPutResponseSchema)
# @required_auth
def user(user_details, user_id):
    # user_details = request.json
    return update_user_details(user_id, user_details)

@bp_users.route('/', methods=['GET'])
@bp_users.arguments(UsersGetRequestSchema, location='query')
@bp_users.response(200, UsersGetResponseSchema)
# @required_auth
def users(query):
    return get_users()

@bp_users.route('/', methods=['POST'])
@bp_users.arguments(UsersPostRequestSchema, location='json')
@bp_users.response(200, UsersPostResponseSchema)
# @required_auth
def users(user_data):
    # user_data = request.json
    return create_user(user_data)