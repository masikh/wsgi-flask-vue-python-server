from flask import request, session, jsonify
from PrivateClasses.Database import Database
from Decorators.Authorization import authorize
from . import routes


@authorize
@routes.route('/api/widgets/get', methods=['GET'])
def api_widgets_get():
    username = session['username']
    database = Database()
    with database:
        result = database.get_widgets(username)
    return jsonify(result)


@authorize
@routes.route('/api/widgets/set', methods=['POST'])
def api_widgets_set():
    data = request.json
    username = session['username']
    database = Database()
    with database:
        result = database.set_widgets(username, data)
    return jsonify(result)
