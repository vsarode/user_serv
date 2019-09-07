from user_service.db.user_models.models import User


def create_user(data):
    user_object = User.objects.create(username=data['username'],
                                      first_name=data['firstName'],
                                      middle_name=data['middleName'],
                                      last_name=data['lastName'],
                                      password=data['password'],
                                      mobile=data['mobile'],
                                      city=data['city'])

    return user_object


def update_user(user, data):
    if 'password' in data:
        user.password = data['password']
    if 'city' in data:
        user.city = data['city']
    if 'mobile' in data:
        user.mobile = data['mobile']
    if 'firstName' in data:
        user.first_name = data['firstName']
    if 'middleName' in data:
        user.middle_name = data['middleName']
    if 'lastName' in data:
        user.last_name = data['lastName']

    user.save()
    return user


def get_users(filters):
    if 'city' in filters:
        user_objects = User.objects.filter(city=filters['city'])
    else:
        user_objects = User.objects.all()
    return user_objects
