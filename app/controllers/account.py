from flask import request

from base import BaseController

from services import UserService


class AccountController(BaseController):
    def routes(self):
        return {
            '/account/login': {
                'post': self.login
            }
        }

    # login
    def login(self):
        data = request.json

        user = UserService().login(data['username'], data['password'])

        return user
