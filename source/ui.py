from PyQt5 import QtWidgets
import sys
import user
from loginScreen import loginScreen

def main():
    app = QtWidgets.QApplication(sys.argv)  
    window = loginScreen()
    app.exec_()

if __name__ == "__main__":
    main()
