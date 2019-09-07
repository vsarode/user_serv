from flask import request, jsonify
from flask_restful import Resource

from user_service.db.user_models.models import User as usr
from user_service.service_api_handler import user_handler
from user_service.utils.user import get_user_dict


class User(Resource):
    def post(self):
        data = request.get_json()
        user_object = user_handler.create_user(data)
        return jsonify({"user": get_user_dict(user_object)})

    def get(self, username=None):
        if username:
            user = usr.objects.get(username=username)
            return jsonify({"user": get_user_dict(user)})

        data = request.args
        user_objects = user_handler.get_users(data)
        return jsonify({"users": [get_user_dict(x) for x in user_objects]})

    def put(self, username):
        data = request.get_json()
        user = usr.objects.get(username=username)
        user = user_handler.update_user(user, data)
        return jsonify({"users": [get_user_dict(user)]})
