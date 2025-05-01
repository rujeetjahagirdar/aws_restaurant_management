from flask import jsonify
from .db import db
from .models import User

def get_user_details(user_id):
    try :
        usr = db.session.get(User, user_id)
        print(usr)
        if (usr):
            return jsonify({"message": {'user_id': usr.user_id, 'user_name': usr.user_name,
                                        'user_contact': usr.user_contact, 'user_email': usr.user_email}}), 200
        else:
            return jsonify({"message": "No users found"}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def update_user_details(user_id, user_details):
    try:
        usr = db.session.get(User, user_id)

        for key, value in user_details.items():
            print(key, value)
            setattr(usr, key, value)

        db.session.commit()
        print(usr.user_contact)
        return jsonify({'message':'User updated successfully!'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

def get_users():

    try:
        users_db = db.session.execute(db.select(User)).scalars().all()
        print(users_db)
        if(users_db):
            users_list = []
            for usr in users_db:
                users_list.append({'user_id': usr.user_id, 'user_name': usr.user_name, 'user_contact': usr.user_contact, 'user_email': usr.user_email})

            return jsonify({"message": users_list}), 200
        else:
            return jsonify({'error': "No users found"}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def create_user(data):
    try:
        new_user = User(user_name = data['name'], user_contact = data['contact'], user_email = data['email'])
        print(new_user)
        db.session.add(new_user)
        db.session.commit()
        if(new_user.user_id):
            return jsonify({'message':f'User created with ID {new_user.user_id}!'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e.orig)})
