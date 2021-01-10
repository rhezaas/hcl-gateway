from requests import request, RequestException, ConnectionError
from base.error import HTTPException


class BaseService:
    def __init__(self, host: str):
        self.__host__: str = host
        self.__method__: str = None
        self.__endpoint__: str = None
        self.__headers__: dict = None
        self.__query__: dict = None
        self.__body__: dict = None

    def get(self, endpoint: str):
        """protected"""
        self.__method__ = 'get'
        self.__endpoint__ = endpoint

        return self

    def post(self, endpoint: str):
        """protected"""
        self.__method__ = 'post'
        self.__endpoint__ = endpoint

        return self

    def put(self, endpoint: str):
        """protected"""
        self.__method__ = 'put'
        self.__endpoint__ = endpoint

        return self

    def delete(self, endpoint: str):
        """protected"""
        self.__method__ = 'delete'
        self.__endpoint__ = endpoint

        return self

    def headers(self, headers: dict):
        """protected"""
        self.__headers__ = headers

        return self

    def query(self, query: dict):
        """protected"""
        self.__query__ = query

        return self

    def body(self, body: dict):
        """protected"""
        self.__body__ = body

        return self

    def send(self):
        """protected"""

        try:
            response = request(
                url=f'{self.__host__}{self.__endpoint__}',
                method=self.__method__,
                headers=self.__headers__,
                params=self.__query__,
                json=self.__body__
            )

            response.raise_for_status()
        except ConnectionError as conenction_err:
            raise HTTPException(500, 'Connection Refused', str(conenction_err))
        except RequestException:
            raise HTTPException(response.status_code, '', response.json())
        else:
            return response.json()
