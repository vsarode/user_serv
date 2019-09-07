def get_user_dict(user_object):
    return {"userName": user_object.username,
            "mobile": user_object.mobile,
            "firstName": user_object.first_name,
            "middleName": user_object.middle_name,
            "lastName": user_object.last_name,
            "createdOn": user_object.created_on.strftime("%d/%m/%Y"),
            "city": user_object.city}
