import os

db = os.getenv('DB', '127.0.0.1')

# Flask server settings
environment = {
    'database': {
        'hostname': 'mongodb://{db}:27017/'.format(db=db),
        'username': 'flask_wsgi_vue',
        'password': 'secret',
        'db_name': 'wsgi_flask_vue_template',
        'db_collections': {'users': ''}
    },
    'key': 'Gnomes are not little friends with pointy hats, hence rather different',
    'flask': {
        'ip_address': '0.0.0.0',
        'port': 8888
    }
}

# Applications working directory
cwd = os.getcwd()

# Global parameters populated in: WSGIServer.app()
global_parameters = {}
