from base import BaseService
from decouple import config


class UserService(BaseService):
    def __init__(self):
        self.__host__ = config('USER_SERVICE_HOST')
        self.__port__ = config('USER_SERVICE_PORT')

        super().__init__(f'{self.__host__}:{self.__port__}')

    def login(self, username: str, password: str):
        return self.post('/account/login')\
            .headers({
                'Content-Type': 'application/json'
            })\
            .body({
                'username': username,
                'password': password
            })\
            .send()

    def getAuth(self, token: str):
        return self.get('/account/auth')\
            .headers({
                'Authorization': f'Bearer {token}'
            })\
            .send()
