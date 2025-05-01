from flask import request, jsonify
from .utils import get_menu, add_menu_item
from flask_smorest import Blueprint
from .schemas import GetMenuQuerySchema, AddMenuRequestSchema, AddMenuResponseSchema, GetMenuResponseSchema

bp_menu = Blueprint('menu_service', __name__, url_prefix='/menu', description= "Menu API")

@bp_menu.route("/", methods=['GET'])
@bp_menu.arguments(GetMenuQuerySchema, location='query')
@bp_menu.response(200, GetMenuResponseSchema)
def getMenu(query):
    return get_menu()


@bp_menu.route("/", methods=['POST'])
@bp_menu.arguments(AddMenuRequestSchema)
@bp_menu.response(200, AddMenuResponseSchema)
def addMenu(data):
    # data = request.json
    item_name = data['item_name']
    item_price = data['item_price']
    item_calories = data['item_calories']

    return add_menu_item(item_name, item_price, item_calories)