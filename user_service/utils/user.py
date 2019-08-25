def get_user_dict(user_object):
    return {"userName": user_object.username,
            "mobile": user_object.mobile,
            "city": user_object.city}
