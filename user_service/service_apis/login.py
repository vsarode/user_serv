from flask import request, jsonify
from flask_restful import Resource

from user_service.service_api_handler import login_handler
from user_service.utils.login import get_login_dict, is_authenticated


class Login(Resource):
    def post(self):
        data = request.get_json()
        return login_handler.create_login(data)

    def get(self):
        token = request.headers.get('token')
        if not token and not is_authenticated(token):
            return "<h1> Unauthenticated User!!</h1>"
        data = request.args
        login_objects = login_handler.get_logins(data)
        return jsonify({"logins": [get_login_dict(x) for x in login_objects]})

    def put(self, token):
        token = request.headers.get('token')
        if not token and not is_authenticated(token):
            return "<h1> Unauthenticated User!!</h1>"
        data = request.args
        login_object = login_handler.update_login(data, token)
        return jsonify({"login": get_login_dict(login_object)})
