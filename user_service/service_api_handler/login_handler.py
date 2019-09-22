import json
import uuid
from datetime import datetime

from flask import make_response

from user_service.db.user_models.models import User, Login
from user_service.utils.login import get_login_dict


def get_logins(data):
    if 'user' in data:
        login_objects = Login.objects.filter(user__username=data['user'])
    else:
        login_objects = Login.objects.all()
    return login_objects


def update_login(data, token):
    login = Login.objects.get(token=token)
    if "action" in data and data['action'] == "logout":
        login.is_active = False
        login.logout_time = datetime.now()
    login.save()
    return login


def is_already_logged_in(user):
    try:
        login_object = Login.objects.get(user=user, is_active=True)
        return True, login_object
    except:
        return False, None


def create_login(data):
    username = data['username']
    password = data['password']
    try:
        user_object = User.objects.get(username=username)
    except:
        return "<h1>Invalid username !!</h1>"
    if user_object.password == password:

        is_logged_in, login_object = is_already_logged_in(user_object)

        if is_logged_in:
            login_object = login_object
        else:
            login_object = Login.objects.create(user=user_object, token=str(uuid.uuid4()))


        response = make_response(json.dumps({"login": get_login_dict(login_object)}))
        response.mimetype = "application/json"
        response.set_cookie("token", login_object.token)

        return response
    else:
        return "<h1> Invalid password !!</h1>"
def get_login(token):
    try:
        login_object = Login.objects.get(token=token)
    except:
        return {"success": False}
    return get_login_dict(login_object)
