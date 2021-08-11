from PyQt5 import QtWidgets, uic
import sys
from mainScreen import mainScreen
import user
class loginScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super(loginScreen, self).__init__()
        uic.loadUi('Login.ui', self)
        self.show()
        self.setFixedSize(self.size())
        self.loginButton.clicked.connect(self.logIn)
        self.mainScreen = None

    def logIn(self):
        address = self.addressLine.text()
        username = self.loginLine.text()
        password = self.passwordLine.text()
        __user = user.user(username, password, address)
        success = __user.init()
        if success:
            self.mainScreen = mainScreen(__user)
            self.mainScreen.show()
            self.close()

