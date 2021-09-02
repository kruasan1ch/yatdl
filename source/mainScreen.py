from PyQt5 import QtWidgets, uic
import sys
import user
from utils import utils

class registrationScreen(QtWidgets.QDialog):
    def __init__(self, __user):
        super(registrationScreen, self).__init__()
        uic.loadUi('Registration.ui', self)
        self.regButton.clicked.connect(self.registrate)
        self._user = __user
        self._utils = utils(self._user.getDb())
        self._users = self._utils.getUsers()
        self.insertUsers()
        self.delButton.clicked.connect(self.deleteUser)

    def insertUsers(self):
        for userData in self._users :
            self.userList.addItem(str(userData))

    def registrate(self):
        username = self.usernameLine.text()
        password = self.passwordLine.text()
        role = self.roleBox.value()
        db = self._user.getDb()
        db.register(username, password, role)
    
    def deleteUser(self):
        item = self.userList.currentItem()
        text = item.text().replace('(','').replace(')','')
        ID = text.split(', ')[0]
        self._utils.deleteUser(ID)
        row = self.userList.currentRow()
        self.userList.takeItem(row)



class mainScreen(QtWidgets.QMainWindow):
    def __init__(self, __user):
        super(mainScreen, self).__init__()
        self._user = __user
        uic.loadUi('MainScreen.ui', self)
        self._utils = utils(self._user.getDb())
        self._users = self._utils.getUsers()
        self._ids = {}
        self._names = {}
        if self._user.getRole() > 0:
            for user in self._users:
                self.comboBox.addItem(str(user[2]))
                self._ids[user[2]] = user[0]
                self._names[user[0]] = user[2]
        else:
            self.comboBox.addItem(str(self._user.getName()))
            self.comboBox.setEnabled(False)
            self._ids[self._user.getName()] = self._user.getId()
            self._names[self._user.getId()] = self._user.getName()
        self.statusBox.addItems(["completed","in work"])
        self.setFixedSize(self.size())
        closeSession = self.actionClose_session
        closeSession.triggered.connect(self.close)
        self.actionRegistration.triggered.connect(self.openRegDialog)
        if self._user.getRole() == 3:
            self.menuAdmin_tools.setEnabled(True)
        self.refreshButton.clicked.connect(self.refresh)
        self.newTaskButton.clicked.connect(self.addTask)
        self.taskList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.deleteButton.clicked.connect(self.deleteTask)
        self.refresh()

    def openRegDialog(self):
        registration = registrationScreen(self._user)
               
        registration.exec_()
        
    def refresh(self):
        self.taskList.clear()
        self.tasks = self._utils.getTasks(self._user.getRole(), self._user.getId())
        separator = "  |  "
        if self.tasks == None:
            pass
        else:
            for task in self.tasks:
                try:
                    item = "" + str(task[0]) + separator + str(task[1]) + separator + str(task[2]) + separator + self._names[task[3]] + separator + task[4]
                except:
                    item = "" + str(task[0]) + separator + str(task[1]) + separator + str(task[2]) + separator + "DELETED" + separator + task[4]
                self.taskList.addItem(item)

    def deleteTask(self):
        item = self.taskList.currentItem()
        text = item.text().replace('(','').replace(')','')
        ID = text.split(', ')[0]
        self._utils.deleteTask(ID)
        self.refresh()

    def addTask(self):
        text = self.lineEdit.text()
        date = self.dateTimeEdit.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        status = self.statusBox.currentText()
        __id = self._ids[self.comboBox.currentText()]
        data = {'time': date, 'text': text, 'ID': __id, 'status': status}
        self._utils.addTask(data)
