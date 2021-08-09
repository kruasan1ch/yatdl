from PyQt5 import QtWidgets, uic 
import sys
import user
class loginScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super(loginScreen, self).__init__()
        uic.loadUi('Login.ui', self)
        self.show()
        self.setFixedSize(self.size())
        self._user = None
        self.loginButton.clicked.connect(self.logIn)

    def logIn(self):
        address = self.addressLine.text()
        username = self.loginLine.text()
        password = self.passwordLine.text()
        self._user = user.user(username, password, address)
        success = self._user.init()
        msg = QtWidgets.QMessageBox()
        msg.setText(str(success))
        msg.exec()

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = loginScreen()
    app.exec_()

if __name__ == "__main__":
    main()
