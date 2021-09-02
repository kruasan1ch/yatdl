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

    def insert(self, data):
        self._sql.execute(f"INSERT INTO tasks (date, task_text, user_id, status) VALUES (?, ?, ?, ?)", (data["time"], data["text"], data["ID"], data["status"]))
        self._db.commit()
    
    def updateData(self, dataLine, ID):
        datetime = dataLine.timestamp.date().isoformat()
        self._sql.execute(f"UPDATE tasks date = ?, task_text = ?, user_id = ?, status = ? WHERE ID = ?", (datetime, dataLine.text, dataLine.userID, dataLine._status, ID))
        self._db.commit()
    
    def delete(self, ID):
        self._sql.execute(f"DELETE FROM tasks WHERE ID = ?", (ID,))
        self._db.commit()

    def isRegistered(self, name, password):
        self._sql.execute(f"SELECT ID FROM users WHERE (user_name = ? AND password = ?)",(name, password))
        if self._sql.fetchone() is None:
            return False
        else:
            return True
    
    def getUserData(self, name):
        self._sql.execute(f"SELECT ID, role FROM users WHERE (user_name = ?)", (name,))
        result = self._sql.fetchone()
        return result

    def getUsers(self):
        self._sql.execute("SELECT * FROM users")
        result = self._sql.fetchall()
        return result
    
    def deleteUser(self, ID):
        self._sql.execute(f"DELETE FROM users WHERE ID = ?", (ID,))
        self._db.commit()

    def getTasks(self, role, ID):
        if role > 0:
            self._sql.execute("SELECT * FROM tasks")
        else:
            self._sql.execute(f"SELECT * FROM tasks WHERE (user_id = ?)", (ID,))
        result = self._sql.fetchall()
        return result

    def register(self, name, password, role):
            self._sql.execute(f"INSERT INTO users (user_name, password, role) VALUES (?, ?, ?)", (name, password, role))
            self._db.commit()
       
