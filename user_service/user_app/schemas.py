from marshmallow import Schema, fields

class UserGetRequestSchema(Schema):
    # user_id = fields.Str(required=False, description= 'User ID for user')
    pass

class UserGetResponseSchema(Schema):
    message = fields.Str(description= "GetUser response message")

class UserPutRequestSchema(Schema):
    # user_id = fields.Str(required=True, description='User ID for user') # no need, since user_id will be in path parameter

    # user_details = fields.Dict(required=True, description= "Nested User details")
    user_name = fields.Str(required=False, description = "User's name")
    user_contact = fields.Str(required=False, description="User's contact")
    user_email = fields.Str(required=False, description="User's email")

class UserPutResponseSchema(Schema):
    message = fields.Str(description= "GetUser response message")

class UsersGetRequestSchema(Schema):
    pass

class UsersGetResponseSchema(Schema):
    message = fields.Str(description="Get all Users response message")

class UsersPostRequestSchema(Schema):
    # user_details = fields.Dict(required=True, description="Nested User details")
    name = fields.Str(required=True, description="User's name")
    contact = fields.Str(required=True, description="User's contact")
    email = fields.Str(required=True, description="User's email")

class UsersPostResponseSchema(Schema):
    message = fields.Str(description="Get all Users response message")