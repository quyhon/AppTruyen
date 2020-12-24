import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QImage, QPalette, QBrush, QIcon, QFont
import view.user.login as login
from controller import signIn, signUp

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600,500)
        self.center()
        self.setWindowTitle('App Truyện')
        self.setWindowIcon(QIcon('./img/icon.jpg'))
        oImage = QImage("./img/login.jpg")
        sImage = oImage.scaled(QSize(600,400))           
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))                        
        self.setPalette(palette)
        self.rootLayout = QHBoxLayout()
        self.setLayout(self.rootLayout)
        login.signInGUI(self)
        # import view.home.homeGUI as home
        # home.homeGUI(self)
        # https://stackoverflow.com/questions/8814452/pyqt-how-to-add-separate-ui-widget-to-qmainwindow
        self.show()

    def center(self):
        """Set Vị Trí Chính Giữa"""
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def clearLayout(self,layout):
        """Clear Layout widget"""
        while layout.count() > 0:
            item = layout.takeAt(0)
            if not item:
                continue
            w = item.widget()
            if w:
                w.deleteLater()
        
    def signInEvent(self):
        """SignIn Event"""
        signIn.event(self)
            
    def signUpEvent(self):
        """Register Event"""
        signUp.event(self)
    
    def backSignInEvent(self):
        """Back SignIn Event"""
        signIn.back(self)

    def registerEvent(self):
        """SignUp Event"""
        signUp.registerEvent(self)