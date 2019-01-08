import threading
from flask import Flask
from routes import *
from wsgiserver import WSGIServer


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
