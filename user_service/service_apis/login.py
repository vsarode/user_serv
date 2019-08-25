from flask import request, jsonify
from flask_restful import Resource

from user_service.db.user_models.models import Login as lgn
from user_service.db.user_models.models import User
from user_service.utils.login import get_login_dict


class Login(Resource):
    def post(self):
        data = request.get_json()
        username = data['username']
        password = data['pass']

        user_objects = User.objects.filter(username=username)

        # comment line
        if not user_objects:
            return "<h1>Invalid username !!</h1>"
        if user_objects[0].password == password:
            login_object = lgn.objects.create(user=user_objects[0])

            return jsonify({"login": get_login_dict(login_object)})

        else:
            return "<h1> Invalid password !!</h1>"
        # this is last statement

    def get(self):
        data = request.args
        if 'user' in data:
            login_objects = lgn.objects.filter(user__username=data['user'])
        else:
            login_objects = lgn.objects.all()

        return jsonify({"logins": [get_login_dict(x) for x in login_objects]})
