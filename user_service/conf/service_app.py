import django;
from flask import Flask


django.setup()

from user_service.service_apis.login import Login
from user_service.service_apis.user import User
from user_service.service_apis.ping import Ping


from flask_restful import Api


app = Flask(__name__)

api = Api(app, prefix='/userservice')

api.add_resource(User, '/user', '/user/<username>')
api.add_resource(Login, '/login', '/login/<token>')
api.add_resource(Ping, '/ping')

if __name__ == '__main__':
    app.run(host='localhost', port=2004, debug=True)
