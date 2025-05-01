from docutils.nodes import description
from marshmallow import Schema, fields

class BookTableRequestSchema(Schema):
    name = fields.Str(required=True, desciption = "Name of the customer making the booking")
    contact = fields.Str(required=True, description = "Contact of the customer making the booking")
    capacity = fields.Int(required=True, description= "Number of guests")
    time = fields.Str(required=True, description = "Time of reservation")

class BookTableResponseSchema(Schema):
    message = fields.Str()


class CheckAvailRequestSchema(Schema):
    capacity = fields.Int(required= True, description = "Capacity of Table")
    time = fields.Str(required=True, description = "Time of reservation")

class CheckAvailResponseSchema(Schema):
    message = fields.Str(description = "Returns Table ID if table available")

class CancelBookingRequestSchema(Schema):
    table_id = fields.Str(required=True, description="Table ID of table to cancel")
    booking_time = fields.Str(required=True, description = "Time of the Booking to cancel")

class CancelBookingResponseSchema(Schema):
    message = fields.Str(description="Booking cancellation message.")