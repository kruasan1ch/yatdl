import dbclass
import datetime
import sqlite3

class sqlitedb(dbclass.dbclass):
    def __init__(self, address):
        self._db = sqlite3.connect(address)
        self._sql = self._db.cursor()

    def get(self):
        self._sql.execute(f"SELECT * FROM tasks WHERE user_id = ? ", (self._user_id, ))
        data = sql.fetchall()
        return data

    def insert(self, dataLine):
        datetime = dataLine.timestamp.date().isoformat()
        self._sql.execute(f"INSERT INTO tasks (date, task_text, user_id, status) VALUES (?, ?, ?, ?)", (datetime, dataLine.text, dataLine.userID, dataLine._status))
        self._db.commit()
    
    def update(self, dataLine, ID):
        datetime = dataLine.timestamp.date().isoformat()
        self._sql.execute(f"UPDATE tasks date = ?, task_text = ?, user_id = ?, status = ? WHERE ID = ?", (datetime, dataLine.text, dataLine.userID, dataLine._status, ID))
        self._db.commit()
    
    def isRegistered(self, name, password):
        self._sql.execute(f"SELECT ID FROM users WHERE (user_name = ? AND password = ?)",(name, password))
        if self._sql.fetchone() is None:
            return False
        else:
            return True

    def register(self, isAdmin, name, password, role):
        if isAdmin:
            self._sql.execute(f"INSERT INTO users (user_name, password, role) VALUES (?, ?, ?)", (name, password, role))
            self._db.commit()
            return True
        else:
            return False
       
