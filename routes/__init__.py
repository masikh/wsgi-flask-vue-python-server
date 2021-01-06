from flask import Blueprint
routes = Blueprint('routes', __name__)

from .authenticate import *
from .index import *
from .api import *
from .user_management import *
