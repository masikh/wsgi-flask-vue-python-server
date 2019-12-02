from . import routes
from flask import jsonify, Response, request
from flask_cors import CORS, cross_origin
from PrivateClasses import ExampleClass
import Configuration
import time
import gevent


@routes.route('/api/user/info', methods=['GET'])
@cross_origin(origin='*', headers=['Access-Control-Allow-Origin', '*'])
def api_user_info():
    """
    summary: Get User info
    ---
    tags:
      - Users

    get:
      parameters:
        - in: query
          name: hostname
          required: False
          schema:
            type: string
            example: 5db8afcda51de479cf481396
          description: Get user information

    responses:
      200:
        description: status message with list of dicts
        content:
          application/json:
            schema:
              type: object

    """
    hostname = 'github.com'
    try:
        hostname = request.query_string('hostname')
        print(hostname)
    except:
        pass
    print(hostname)
    example_class = ExampleClass(hostname,
                                 Configuration.global_parameters['home_dir'],
                                 Configuration.global_parameters['username'])
    value = example_class.example()
    return jsonify(value)


@routes.route('/api/sse')
@cross_origin(origin='*', headers=['Access-Control-Allow-Origin', '*'])
def api_sse():
    def inner():
        sse_emit = True
        while sse_emit:
            try:
                status = str(time.time())
                data = 'data: {text}\n\n'.format(text=status)
                yield data
                gevent.sleep(0.1)
            except GeneratorExit:
                yield 'data: END-OF-STREAM\n\n'
                raise GeneratorExit
            finally:
                sse_emit = False

    try:
        return Response(inner(), mimetype='text/event-stream')
    except Exception as error:
        print('Caught error in /sse-emitter: {error}'.format(error=error))
        return Response('data: END-OF-STREAM\n\n', mimetype='text/event-stream')
