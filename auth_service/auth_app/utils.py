import boto3
from flask import jsonify, current_app
import hmac
import hashlib
import base64
from config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, DEFAULT_REGION, USER_POOL_ID
import jwt
import time

cognito_client = boto3.client('cognito-idp', region_name=DEFAULT_REGION, aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

EXPECTED_ISSUER = f"https://cognito-idp.{DEFAULT_REGION}.amazonaws.com/{USER_POOL_ID}"

def get_secret_hash(username):
    client_id = current_app.config.get('COGNITO_CLIENT_ID')
    client_secret = current_app.config.get('COGNITO_CLIENT_SECRET')
    message = username + client_id
    dig = hmac.new(
        client_secret.encode("utf-8"),
        message.encode("utf-8"),
        hashlib.sha256
    ).digest()
    return base64.b64encode(dig).decode()


def cognito_signup(data):
    usrnm = data['username']
    passwd = data['password']
    try:
        response = cognito_client.sign_up(
            ClientId = current_app.config.get('COGNITO_CLIENT_ID'),
            SecretHash = get_secret_hash(usrnm),
            Username = usrnm,
            Password = passwd,
            UserAttributes = [
                {
                    'Name':'email',
                    'Value':data['email']
                }
            ]

        )
        return jsonify({'message':"User create successfully!!"}), 200
    except cognito_client.exceptions.UsernameExistsException:
        return jsonify({'error':"User already exists"}), 409
    except Exception as e:
        return jsonify({'error':e}), 500

def cognito_get_users():
    try:
        response = cognito_client.list_users(
            UserPoolId = USER_POOL_ID,
            AttributesToGet=[
                'email'
            ]
        )

        return response
    except cognito_client.exceptions.ResourceNotFoundException:
        return jsonify({'error':' Resource Not found'}), 500
    except Exception as e:
        return jsonify({'error':e}), 500

def cognito_login(data):
    try:
        response = cognito_client.initiate_auth(
            AuthFlow = 'USER_PASSWORD_AUTH',
            ClientId = current_app.config.get('COGNITO_CLIENT_ID'),
            AuthParameters = {
                "USERNAME": data["username"],
                "PASSWORD": data["password"],
                "SECRET_HASH" : get_secret_hash(data["username"])
            }
        )
        print(response)
        return jsonify({'message':'User authenticated!!!'}), 200
    except cognito_client.exceptions.NotAuthorizedException:
        return jsonify({'error':"User is not authorized"}), 401
    except Exception as e:
        return jsonify({'error': e}), 500

def cognito_verify_token(tkn):
    try:
        decoded_tkn = jwt.decode(tkn, options={"verify_signature":False})

        exp = decoded_tkn.get("exp")
        if not exp or int(exp) < int(time.time()):
            return jsonify({"error": "Token expired"}), 401

        iss = decoded_tkn.get("iss")
        if iss != EXPECTED_ISSUER:
            return jsonify({"error": "Invalid issuer"}), 401

        token_use = decoded_tkn.get("token_use")
        if token_use != "access":
            return jsonify({"error": "Invalid token_use"}), 401

        client_id = decoded_tkn.get("client_id")
        if client_id != current_app.config.get('COGNITO_CLIENT_ID'):
            return jsonify({"error": "Invalid client_id"}), 401

        return jsonify(decoded_tkn), 200

    except Exception as e:
        return jsonify({"error": "Invalid Token"}), 401