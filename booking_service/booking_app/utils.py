from flask import current_app, jsonify
import requests


def check_availability(capacity, time):
    tables_db = current_app.config.get('tables_db')
    for key, values in tables_db.items():
        if (values['capacity'] >= capacity and values['booking_time'] == None):
            return jsonify({'message':key}), 200
    return jsonify({'error':'No table available'}), 404

def book_table(name, contact, number_of_guests, time):
    tble_id_response = requests.get('http://127.0.0.1:5002/booking/check_availability',
                                    params={'capacity': number_of_guests, 'time': time})

    if (tble_id_response.status_code == 200):
        tble_id = str(tble_id_response.json()['message'])
        print(tble_id)

        tables_db = current_app.config.get('tables_db')
        tables_db[tble_id]['booking_time'] = time
        return jsonify({'message': f'Table {tble_id} Booked Successfully !!!'}), 200
    else:
        return jsonify({'error': tble_id_response.json()}), 404

def cancel_booking(table_id, booking_time):
    tables_db = current_app.config.get('tables_db')

    if(tables_db[str(table_id)]['booking_time']!=None):
        tables_db[str(table_id)]['booking_time'] = None
        return jsonify({'message': f'Booking for {table_id} cancelled Successfully !!!'}), 200
    else:
        return jsonify({'error':'Specified table is not booked.'}), 400


