from user_service.utils.user import get_user_dict


def get_login_dict(login_object):
    return {"user": get_user_dict(login_object.user),
            'loginTime': login_object.login_time.strftime('%d/%m/%Y')}
