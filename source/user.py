import sqlite3

class user:
    def __init__(self, userid, username, password, role, dbpath):
        self._user_id = userid
        self._user_name = username 
        self._user_pass = password
        self._user_role = role
        self._db = sqlite3.connect(dbpath)
        self._sql = self._db.cursor()

    @property
    def _user_id(self):
        return self._user_id
    
    @property
    def _user_role(self):
        return self._user_role

    def getData()
        self._sql.execute(f"SELECT * FROM tasks WHERE user_id = ? ", (self._user_id, ))
        data = sql.fetchall()
        return data
