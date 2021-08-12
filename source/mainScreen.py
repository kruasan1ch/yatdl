from PyQt5 import QtWidgets, uic
import sys
import user

class registrationScreen(QtWidgets.QDialog):
    def __init__(self, __user):
        super(registrationScreen, self).__init__()
        uic.loadUi('Registration.ui', self)
        self.regButton.clicked.connect(self.registrate)
        self._user = __user
        self._users = self._user.getUsers()
        self.insertUsers()

    def insertUsers(self):
        for userData in self._users :
            self.userList.addItem(str(userData))

    def registrate(self):
        username = self.usernameLine.text()
        password = self.passwordLine.text()
        role = self.roleBox.value()
        db = self._user.getDb()
        db.register(username, password, role)


class mainScreen(QtWidgets.QMainWindow):
    def __init__(self, __user):
        super(mainScreen, self).__init__()
        self._user = __user
        uic.loadUi('MainScreen.ui', self)
        self.setFixedSize(self.size())
        closeSession = self.actionClose_session
        closeSession.triggered.connect(self.close)
        self.actionRegistration.triggered.connect(self.openRegDialog)
        if self._user.getRole() == 3:
            self.menuAdmin_tools.setEnabled(True)

    def openRegDialog(self):
        registration = registrationScreen(self._user)
               
        registration.exec_()

