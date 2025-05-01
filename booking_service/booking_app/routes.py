from flask import request
from .utils import check_availability, book_table, cancel_booking
from .schemas import BookTableRequestSchema, BookTableResponseSchema, CheckAvailRequestSchema, CheckAvailResponseSchema, CancelBookingRequestSchema, CancelBookingResponseSchema
from flask_smorest import Blueprint

bp_availability = Blueprint('booking', __name__, url_prefix='/booking', description="Booking Operations")

@bp_availability.route('/check_availability', methods=['GET'])
@bp_availability.arguments(CheckAvailRequestSchema, location='query')
@bp_availability.response(200, CheckAvailResponseSchema)
def check_avail(data):
    if(request.method=='GET'):
        # capacity = int(request.args.get('capacity'))
        # time = request.args.get('time')
        capacity = data['capacity']
        time = data['time']

        return check_availability(capacity, time)

@bp_availability.route('/book_table', methods=['POST'])
@bp_availability.arguments(BookTableRequestSchema)
@bp_availability.response(200, BookTableResponseSchema)
def book(data):
    if(request.method=='POST'):
        # data = request.json
        user_name = data['name']
        contact = data['contact']
        capacity = data['capacity']
        time = data['time']

        return book_table(user_name, contact, capacity, time)

@bp_availability.route('/cancel_booking', methods=['POST'])
@bp_availability.arguments(CancelBookingRequestSchema, location='json')
@bp_availability.response(200, CancelBookingResponseSchema)
def cancel(data):
    if(request.method=='POST'):
        # data =  request.json
        tble_id = data['table_id']
        booking_time = data['booking_time']

        return cancel_booking(tble_id, booking_time)
