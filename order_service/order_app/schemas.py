from marshmallow import Schema, fields

class OrderRequestSchema(Schema):
    item = fields.Str(required=True, description= "Item name")
    quantity = fields.Int(required=True, description= "Quantity of Item")
    notes = fields.Str(required=True, description= "Notes for Order")

class OrderResponseSchema(Schema):
    message = fields.Str(description= "Order response message")


class CancelRequestSchema(Schema):
    order_id = fields.Str(required= True, description = "Order ID to be cancelled")

class CancelResponseSchema(Schema):
    message = fields.Str(description= "Cancel response message")

class GetInvRequestSchema(Schema):
    item_name = fields.Str(required=False, desription= "Item name to check in inventory")

class GetInvResponseSchema(Schema):
    message = fields.Str(description="Get Inventory response message")

class GetOrdRequestSchema(Schema):
    order_id = fields.Str(required=False, description="Order ID to get order details for")

class GetOrderResponseSchema(Schema):
    message = fields.Str(description="Get Inventory response message")