from flask import Blueprint
routes = Blueprint('routes', __name__)

from .index import *
from .api import *
from .web import *
