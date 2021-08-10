from PyQt5 import QtWidgets, uic
import sys
import user

class mainScreen(QtWidgets.QMainWindow):
    def __init__(self, __user):
        super(mainScreen, self).__init__()
        self._user = __user
        uic.loadUi('MainScreen.ui', self)
        self.setFixedSize(self.size())
        print(self._user.getName())
