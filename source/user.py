import sqlitedb

class user:
    def __init__(self, userid, username, password, role, dbaddress):
        self._user_id = userid
        self._user_name = username 
        self._user_pass = password
        self._user_role = role
        self._db = sqlitedb(dbaddress)

    @property
    def _user_id(self):
        return self._user_id
    
    @property
    def _user_role(self):
        return self._user_role
    @property
    def _getDb():
        return self._db
