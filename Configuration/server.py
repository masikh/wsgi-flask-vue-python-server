import os

# Flask server settings
environment = {'ip': '0.0.0.0',
               'port': 5000}

# Applications user settings
username = 'masikh' 
home_directory = '/home/masikh'

# Applications working directory
cwd = os.getcwd()

# Global parameters populated in: WSGIServer.app()
global_parameters = {}
