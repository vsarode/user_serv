from flask import request, jsonify
from flask_restful import Resource
from user_service.db.user_models.models import User as usr
from user_service.utils.user import get_user_dict


class User(Resource):
    def post(self):
        data = request.get_json()
        user_object = usr.objects.create(username=data['username'],
                                          password=data['pass'],
                                          mobile=data['mobile'],
                                          city=data['city'])
        # user_res = {"userName": user_object.username,
        #             "mobile": user_object.mobile,
        #             "city": user_object.city}
        #
        # return jsonify({"user": user_res})

        return jsonify({"user": get_user_dict(user_object)})

    def get(self, username=None):
        # user_list = []
        data = request.args
        if username:
            user = usr.objects.get(username=username)
            return jsonify({"user": get_user_dict(user)})
        if 'city' in data:
            user_objects = usr.objects.filter(city=data['city'])
        else:
            user_objects = usr.objects.all()

        # for user_object in user_objects:
        #     res = {"userName":
        #                user_object.username,
        #             "mobile": user_object.mobile,
        #             "city": user_object.city}
        #
        #     user_list.append(get_user_dict(user_object))

        # user_res = [get_user_dict(x) for x in user_objects]

        # return jsonify({"users": user_list})
        # return jsonify({"users": user_res})
        return jsonify({"users": [get_user_dict(x) for x in user_objects]})
