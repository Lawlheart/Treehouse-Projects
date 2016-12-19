from flask import Blueprint, abort

from flask.ext.restful import (Resource, Api, reqparse, inputs, fields,
                               marshal, marshal_with, url_for)
import models

user_fields = {
    'username': fields.String,
    'email': fields.String,
    'password': fields.String
}


class UserList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'username',
            required=True,
            help='No Username Provided',
            location=['form', 'json'])
        self.reqparse.add_argument(
            'email',
            required=True,
            help='No email Provided',
            location=['form', 'json'])
        self.reqparse.add_argument(
            'password',
            required=True,
            help='No Password Provided',
            location=['form', 'json'])
        super().__init__()

    def get(self):
        users = models.User.select()


users_api = Blueprint('resources.users', __name__)
api = Api(users_api)
api.add_resource(UserList, '/users', endpoint='users')