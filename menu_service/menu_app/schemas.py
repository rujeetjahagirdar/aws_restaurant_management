from marshmallow import Schema, fields

class GetMenuQuerySchema(Schema):
    # item_name = fields.Str(required=False, description= "Item name")
    pass
class GetMenuResponseSchema(Schema):
    item_name = fields.Str(description="Menu Item name")
    item_price = fields.Str(description="Menu Item Price")
    item_calories = fields.Str(description="Item Calories")

class AddMenuRequestSchema(Schema):
    item_name = fields.Str(required=True, description= "Menu Item name")
    item_price = fields.Int(required=True, description= "Menu Item Price")
    item_calories = fields.Int(required=True, description = "Item Calories")

class AddMenuResponseSchema(Schema):
    message = fields.Str()
