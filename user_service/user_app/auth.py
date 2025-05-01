from functools import wraps
from flask import request, jsonify
import requests

def required_auth(f):
    @wraps(f)
    def verify_user_token(*args, **kwargs):
        user_token = request.headers.get("Authorization")
        # print(user_token)
        header = {
            "Authorization": user_token
        }
        result = requests.get('http://127.0.0.1:5001/auth/verify_token', headers=header)
        print(result.json())
        if(result.status_code==200):
            return f(*args, **kwargs)
        else:
            return jsonify({"error":"Unauthorized "}), 401
    return verify_user_token