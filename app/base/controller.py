from base.error import BaseError
from flask import make_response


class BaseController:
    def __init__(self, server):
        self.mapRoute(server)

    def routes(self) -> dict:
        pass

    def mapRoute(self, server):
        routes = self.routes()

        for route in routes:
            for method in routes[route]:
                server.route(route, methods=[method.upper()])(self.transaction(routes[route][method]))  # noqa: E501

    def transaction(self, function):
        def wrapper():
            try:
                return function()
            except BaseError as e:
                return self.exception(e.__dict__)

        wrapper.__name__ = function.__name__
        return wrapper

    def exception(self, error):
        return make_response(error, error['code'])  # noqa: E501
