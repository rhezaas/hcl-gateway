from waitress import serve
from flask import Flask
import controllers


class Server():
    def __init__(self):
        self.__flask__ = Flask('Gateway')

    def config(self):
        self.__flask__.config['JSON_SORT_KEYS'] = False
        self.__flask__.route('/', methods=['GET'])(lambda: 'Gateway service is running')  # noqa: E501

        return self

    def serveRoutes(self):
        for controller in controllers.__all__:
            controller(self.__flask__)

        return self

    def run(self):
        serve(self.__flask__)
