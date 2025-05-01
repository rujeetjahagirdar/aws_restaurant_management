from flask import current_app, jsonify

def check_inventory(item, quantity):
    inventory_db = current_app.config.get('inventory_db')
    if(item in inventory_db):
        if(inventory_db[item]>=quantity):
            return True
    return False

def get_inventory():
    inventory_db = current_app.config.get('inventory_db')

    return jsonify({'message': inventory_db}), 200

def get_orders():
    orders = current_app.config.get('orders_db')

    return jsonify({'message': orders}), 200

def place_order(item, quantity, notes):
    inventory_db = current_app.config.get('inventory_db')
    orders_db = current_app.config.get('orders_db')
    if(check_inventory(item, quantity)):
        inventory_db[item] -=quantity
        order_id = f'ORD{current_app.config.get('order_id_int')+1}'
        current_app.config['order_id_int']+=1
        orders_db[order_id] = {'item': item, 'quantity': quantity, 'status': 'placed'}

        return jsonify({'message': f'Order placed with order ID {order_id}'}), 200
    else:
        return jsonify({"error": "Can not place order, item/quantity not available"}), 404

def cancel_order(order_id):
    orders_db = current_app.config.get('orders_db')
    inventory_db = current_app.config.get('inventory_db')

    if(order_id in orders_db):
        order_item = orders_db[order_id]['item']
        order_quantity = orders_db[order_id]['quantity']
        orders_db[order_id]['status'] = 'cancelled'
        inventory_db[order_item]+= int(orders_db[order_id]['quantity'])

        return jsonify({'message': f'Order {order_id} cancelled'}), 200
    else:
        return jsonify({"error": "Order not found"}), 404