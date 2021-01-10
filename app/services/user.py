from base import BaseService


class UserService(BaseService):
    def __init__(self):
        super().__init__('http://localhost:8081')

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
