from sqlitedb import sqlitedb

class utils:
    def __init__(self, database):
        self._db = database

    def getUsers(self):
        return self._db.getUsers()

    def deleteUser(self, ID):
        self._db.deleteUser(ID)

    def getTasks(self, userRole, userId):
        return self._db.getTasks(userRole, userId)

    def addTask(self, data):
        self._db.insert(data)

    def deleteTask(self, ID):
        self._db.delete(ID)
