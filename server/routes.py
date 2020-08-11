from .index_controller import IndexController

from kao_flask import Endpoint

routes = [
    Endpoint('/', get=IndexController()),
]
