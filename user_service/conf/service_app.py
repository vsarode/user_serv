import django;
from flask import Flask, request, jsonify

django.setup()
from user_service.db.user_models.models import User

app = Flask(__name__)


@app.route('/ping')
def ping():
    return "Up!!"


@app.route('/signup')
def signup():
    data = request.args
    user_object = User.objects.create(username=data['username'],
                                      password=data['pass'],
                                      mobile=data['mobile'],
                                      city=data['city'])
    user_res = {"username": user_object.username,
                "mobile": user_object.mobile,
                "city": user_object.city}

    return jsonify({"user": user_res})


@app.route('/login')
def login():
    data = request.args
    username = data['username']
    password = data['pass']

    user_objects = User.objects.filter(username=username)

    if not user_objects:
        return "<h1>Invalid username !!</h1>"
    if user_objects[0].password == password:
        return "<h1>Login successfully !!</h1>"
    else:
        return "<h1> Invalid password !!</h1>"


if __name__ == '__main__':
    app.run(host='localhost', port=2004, debug=True)
