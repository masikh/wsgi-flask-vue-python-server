class ExampleClass:
    def __init__(self, hostname='Localhost', homedir=None, username=None, debug=False):
        self.hostname = hostname
        self.homedir = homedir
        self.username = username
        self.debug = debug

    def example(self):
        try:
            return {'hostname': self.hostname, 'username': self.username, 'homedir': self.homedir}
        except Exception as error:
            if self.debug:
                print(error)
        return {}
