from sqlitedb import sqlitedb

class user:
    def __init__(self, username, password, dbaddress):
        self._userId = None
        self._userName = username 
        self._userPass = password
        self._userRole = None
        self._db = sqlitedb(dbaddress)

    def init(self):
        if self._db.isRegistered(self._userName, self._userPass) == 1:
            return True
        else:
            return False
    def getName(self):
        return self._userName

    def getId(self):
        return self._userId
    
    def getRole(self):
        return self._userRole

    def getDb():
        return self._db
