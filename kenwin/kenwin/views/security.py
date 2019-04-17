import bcrypt
from pyramid.security import Allow, Everyone, Authenticated


class AdminSecurity(object):
    __acl__ = [(Allow, Everyone, 'view'),
               (Allow, Authenticated, 'admin_view')]

    def __init__(self, request):
        pass


def hash_password(pw):
    pwhash = bcrypt.hashpw(pw.encode('utf8'), bcrypt.gensalt())
    return pwhash.decode('utf8')


def check_password(pw, hashed_pw):
    expected_hash = hashed_pw.encode('utf8')
    return bcrypt.checkpw(pw.encode('utf8'), expected_hash)
