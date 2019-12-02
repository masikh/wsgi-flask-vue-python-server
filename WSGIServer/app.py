import threading
import time
import yaml
import Configuration
from flask import Flask
from routes import *
from wsgiserver import WSGIServer
from flasgger import Swagger

template = {
  "swagger": "2.0",
  "info": {
    "title": "Example WSI-Flask-server",
    "description": "API Example WSI-Flask-server",
    "contact": {
      "responsibleOrganization": "Your Organization",
      "responsibleDeveloper": "Robert Nagtegaal",
      "email": "masikh@gmail.com",
      "url": "http://github.com/masikh",
    },
    "version": "version-0.1"
  },
  "host": "{HOSTIP}:5000".format(HOSTIP=Configuration.environment['ip']),
  "basePath": "",
  "schemes": [
    "http"
  ],
  "security": [
    {
        "APIKeyAuth": []
    }
  ],
  "static_url_path": "/flasgger",
  "description": "Example WSI-Flask-server, powered by WSGI-Flask",
  "operationId": "getmyData"
}


class ConfigClass(object):
    """ Flask application config
    """
    JSON_SORT_KEYS = True
    JSONIFY_PRETTYPRINT_REGULAR = True
    TEMPLATES_AUTO_RELOAD = True
    SECRET_KEY = 'gGhHjJkK687809132465{timestamp}'.format(timestamp=time.time())
    SWAGGER = {
        'title': 'Example WSI-Flask-server',
        'uiversion': 3
    }


class APIServer:
    def __init__(self, ip, port, cwd, home_dir, username, debug=False):
        self.ip = ip
        self.port = port
        self.cwd = cwd
        self.home_dir = home_dir
        self.username = username
        self.debug = debug
        Configuration.global_parameters = self.__dict__
        self.app = Flask('WSGI-Flask Server on port: {port}'.format(port=self.port),
                         template_folder='{}/templates'.format(self.cwd),
                         static_folder='{}/static'.format(self.cwd))
        self.http_server = None

        # Start the API documentation services
        try:
            yaml.warnings({'YAMLLoadWarning': False})
        except Exception as error:
            print(error)
        Swagger(self.app, template=template)

        # Allow cors for /api and /apidocs
        CORS(self.app, resources={r"/api/*": {"origins": "*"}, r"/apidocs/*": {"origins": "*"}})

        threading.Thread(target=self.run).start()

    def run(self):
        print('Starting WSGI-Flask Server on port: {port}'.format(port=self.port))
        print('API: http://{}:{}'.format(self.ip, self.port))
        self.app.config['JSON_SORT_KEYS'] = True
        self.app.config['TEMPLATES_AUTO_RELOAD'] = True
        self.app.config['SECRET_KEY'] = str(time.time())
        self.app.debug = True
        self.app.register_blueprint(routes)


        self.http_server = WSGIServer(self.app, host=self.ip, port=self.port)
        self.http_server.start()

    def stop(self):
        self.http_server.stop()
