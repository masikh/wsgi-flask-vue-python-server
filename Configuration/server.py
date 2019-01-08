import os

# Flask server settings
environment = {'ip': '0.0.0.0',
               'port': 5000}

# Applications user settings
username = os.environ['USER']
home_directory = os.path.realpath(os.path.expanduser('~{}'.format(username)))

# Applications working directory
cwd = os.getcwd()

# Global parameters populated in: WSGIServer.app()
global_parameters = {}
