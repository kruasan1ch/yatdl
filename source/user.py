from sqlitedb import sqlitedb

class user:
    def __init__(self, username, password, dbaddress):
        self._user_id = None
        self._user_name = username 
        self._user_pass = password
        self._user_role = None
        self._db = sqlitedb(dbaddress)

    def init(self):
        if self._db.isRegistered(self._user_name, self._user_pass) == 1:
            return True
        else:
            return False

    def _user_id(self):
        return self._user_id
    
    def _user_role(self):
        return self._user_role

    def _getDb():
        return self._db
