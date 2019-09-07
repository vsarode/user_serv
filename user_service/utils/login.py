from user_service.utils.user import get_user_dict


def get_login_dict(login_object):
    return {"user": get_user_dict(login_object.user),
            'loginTime': login_object.login_time.strftime('%d/%m/%Y'),
            "logOutTime": login_object.logout_time.strftime('%d/%m/%Y') if login_object.logout_time else "NA",
            "isActive": login_object.is_active,
            "token":login_object.token}
