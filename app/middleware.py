from flask import request
from services import UserService
from error import UnauthorizedException, NeedAutorizationException
from inspect import getargspec


class Middleware:
    @staticmethod
    def authentication(function):
        def wrapper(self):
            try:
                token = request.headers['Authorization'].split(' ')[1]

                user = UserService().getAuth(token)

                if not (user is None):
                    if 'user' in getargspec(function)[0]:
                        return function(self, user)
                    else:
                        return function(self)
                else:
                    raise UnauthorizedException('')
            except Exception:
                raise NeedAutorizationException('')

        wrapper.__name__ = function.__name__
        return wrapper
