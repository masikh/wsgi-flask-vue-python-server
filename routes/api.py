from . import routes
from flask import jsonify, Response
from PrivateClasses import ExampleClass
import Configuration
import time
import gevent


@routes.route('/api/userinfo')
def api_userinfo():
    example_class = ExampleClass(Configuration.global_parameters['ip'],
                                 Configuration.global_parameters['home_dir'],
                                 Configuration.global_parameters['username'])
    value = example_class.example()
    return jsonify(value)


@routes.route('/api/sse')
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
                sse_emit = False
                yield 'data: END-OF-STREAM\n\n'

    try:
        return Response(inner(), mimetype='text/event-stream')
    except Exception as error:
        print('Caught error in /sse-emitter: {error}'.format(error=error))
        return Response('data: END-OF-STREAM\n\n', mimetype='text/event-stream')