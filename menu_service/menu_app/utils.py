from flask import current_app, jsonify

def get_menu():
    # print(current_app.config["menu_db"])
    menu_items = current_app.config.get('menu_db', {})
    return jsonify({'message': menu_items}), 200

def add_menu_item(item_name, item_price, item_calories):
    menu_items = current_app.config.setdefault('menu_db', {})
    menu_items[item_name] = {'price': item_price, 'calories': item_calories}
    # current_app.config["menu_db"] = menu_items
    # print(current_app.config["menu_db"])
    return jsonify({'message': "Item added to menu"}), 200