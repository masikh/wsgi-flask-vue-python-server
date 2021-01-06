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

    """ Connect to db and create collections if they don't exist and set access rights
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
                from PrivateClasses.UserManagement import Users
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
        except OperationFailure:
            pass
        except TypeError:
            pass
        except AttributeError:
            pass
        self.database = None
        self.client = None

    """ Users management
    """

    def user_add(self, session_user=None, username=None, password_hash=None, admin=None):
        # Missing parameter? Bailout.
        if not all([x for x in [session_user, username, password_hash, admin] if x is None]):
            return {'status': False, 'message': 'Missing parameter'}

        # Check if user is admin
        if self.database.users.find_one({'username': session_user, 'admin': True}) is None:
            return {'status': False, 'message': 'Insufficient access rights'}

        # Does this user exist?
        user = self.database.users.find_one({'username': username})
        if user is None:
            self.database.users.insert_one({'username': username, 'password_hash': password_hash, 'admin': admin})
            return {'status': True, 'message': 'User {username} created'.format(username=username)}
        return {'status': False, 'message': 'User already exist'}

    def user_del(self, session_user=None, username=None):
        # Missing parameter? Bailout.
        if not all([x for x in [session_user, username] if x is None]):
            return {'status': False, 'message': 'Missing parameter'}

        # Check if user is admin or actual user
        if self.database.users.find_one({'username': session_user, 'admin': True}) is None:
            return {'status': False, 'message': 'Insufficient access rights'}

        # Does this user exist?
        user = self.database.users.find_one({'username': username})
        if user is None:
            return {'status': False, 'message': 'No such user'}

        # Is this the last admin user?
        elif user['admin'] is True and self.database.users.find({'admin': True}).count() == 1:
            return {'status': False, 'message': 'Refused to delete last admin user'}

        # Remove the user
        else:
            self.database.users.delete_one({'username': username})
            return {'status': True, 'message': 'User {username} deleted'.format(username=username)}

    def user_set_password(self, session_user=None, password_hash=None):
        # Missing parameter? Bailout.
        if not all([x for x in [session_user, password_hash] if x is None]):
            return {'status': False, 'message': 'Missing parameter'}

        # Update the user
        self.database.users.update({'username': session_user}, {'$set': {'password_hash': password_hash}})
        return {'status': True, 'message': 'Password for {username} changed'.format(username=session_user)}

    def user_set_admin(self, session_user=None, username=None, admin=None):
        # Missing parameter? Bailout.
        if not all([x for x in [session_user, username, admin] if x is None]):
            return {'status': False, 'message': 'Missing parameter'}

        # Only allow admin users to make changes
        if self.database.users.find_one({'username': session_user, 'admin': True}) is None:
            return {'status': False, 'message': 'Insufficient access rights'}

        # If we're the last admin, bailout, we don't like to fall out of the tree!
        if self.database.users.find({'admin': True}).count() == 1 and admin is False:
            return {'status': False, 'message': 'Refused to delete last admin user'}

        # Update the user
        self.database.users.update({'username': username}, {'$set': {'admin': admin}})
        return {'status': False,
                'message': 'Access for {username} set to: {admin}'.format(username=username,
                                                                          admin='admin' if admin is True else 'user')}

    def user_set_token(self, session_user=None, token=None):
        if not all([x for x in [session_user, token] if x is None]):
            return {'status': False, 'message': 'Missing parameter'}

        user = self.database.users.find_one({'username': session_user})
        # Does this user exist?
        if user is None:
            return {'status': False, 'message': 'No such user'}
        else:
            self.database.users.update({'username': session_user}, {'$set': {'token': token}})
            return {'status': True, 'message': 'Token updated'}

    def user_query(self, username=None):
        # Missing parameter? Bailout.
        if not all([x for x in [username] if x is None]):
            return {'status': False, 'message': 'Missing parameter'}

        # Query this user
        user = self.database.users.find_one({'username': username}, {'_id': False})
        if user is None:
            return {'status': False, 'message': 'No such user'}
        return {'status': True, 'message': user}

    def users_query(self):
        return {'status': True,
                'message': list(self.database.users.find({},
                                                         {'_id': False,
                                                          'token': False,
                                                          'password_hash': False}))}