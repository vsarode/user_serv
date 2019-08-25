import django;
from flask import Flask


django.setup()

from flask_restful import Api
from user_service.service_apis.login import Login
from user_service.service_apis.user import User


app = Flask(__name__)

api = Api(app)

api.add_resource(User, '/user', '/user/<username>')
api.add_resource(Login, '/login')

if __name__ == '__main__':
    app.run(host='localhost', port=2004, debug=True)
