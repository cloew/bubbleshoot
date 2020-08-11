from .config import DevelopmentConfig
from .routes import routes

from kao_flask import Server

import os

server = Server(__name__, config=DevelopmentConfig, routes=routes)
