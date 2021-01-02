from Configuration import environment
from pymongo import MongoClient
from pymongo.errors import OperationFailure, ServerSelectionTimeoutError


class Database:
    def __init__(self):
        self.settings = environment['database']
        self.client = None
        self.database = None

    def __enter__(self):
        self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

    """ Create collections if they don't exist and set access rights
    """
    def connect(self):
        try:
            self.client = MongoClient(self.settings['hostname'],
                                      username=self.settings['username'],
                                      password=self.settings['password'],
                                      authSource='admin',
                                      authMechanism='SCRAM-SHA-1')

            # Check if db has been initialized before
            db_list = self.client.list_database_names()
            self.database = self.client[self.settings['db_name']]
            if self.settings['db_name'] not in db_list:
                from PrivateClasses.Users import Users
                default_credentials = {'username': 'admin', 'password_hash': Users().hash_password('admin')}
                self.database['users'].insert(default_credentials)
        except OperationFailure as error:
            print('Caught error in Database.connect(): {error}'.format(error=error))
            self.disconnect()

    """ Disconnect from database
    """
    def disconnect(self):
        try:
            self.client.close()
        except ServerSelectionTimeoutError:
            pass
        except OperationFailure as error:
            pass
        except TypeError:
            pass
        except AttributeError:
            pass
        self.database = None
        self.client = None

    """ Add/Delete and query user
    """
    def users(self, payload, add=False, delete=False):
        try:
            if add is True:
                self.database.users.delete_many({'username': payload['username']})
                self.database.users.insert_one(payload)
            elif delete is True:
                self.database.users.delete_one({'username': payload['username']})
            else:
                return self.database.users.find_one(payload, {'_id': False})

        except OperationFailure as error:
            return {'status': False, 'message': str(error)}
        except TypeError as error:
            return {'status': False, 'message': str(error)}

