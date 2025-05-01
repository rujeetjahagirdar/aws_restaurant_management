from flask import request
from .utils import cancel_order, place_order, get_orders, get_inventory
from flask_smorest import Blueprint
from .schemas import OrderRequestSchema, OrderResponseSchema, CancelRequestSchema, CancelResponseSchema, GetInvRequestSchema, GetInvResponseSchema, GetOrdRequestSchema, GetOrderResponseSchema


bp_order = Blueprint('order', __name__, url_prefix='/order')

@bp_order.route('/place_order', methods=['POST'])
@bp_order.arguments(OrderRequestSchema, location='json')
@bp_order.response(200, OrderResponseSchema)
def order(data):
    # data = request.json
    item = data['item']
    quantity = int(data['quantity'])
    notes = data['notes']
    return place_order(item, quantity, notes)


@bp_order.route('/cancel_order', methods=['POST'])
@bp_order.arguments(CancelRequestSchema, location='json')
@bp_order.response(200, CancelResponseSchema)
def cancel(data):
    # data = request.json
    order_id = data['order_id']

    return cancel_order(order_id)

@bp_order.route('/get_inventory', methods=['GET'])
@bp_order.arguments(GetInvRequestSchema, location='query')
@bp_order.response(200, GetInvResponseSchema)
def get_inv(query):
    return get_inventory()

@bp_order.route('/get_orders', methods=['GET'])
@bp_order.arguments(GetOrdRequestSchema, location='query')
@bp_order.response(200, GetOrderResponseSchema)
def get_ord(query):
    return get_orders()