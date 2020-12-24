import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QImage, QPalette, QBrush, QIcon, QFont

class home(QMainWindow):
    def __init__(self):
        super().__init__()

    def homeGUI(self):
        self.resize(600,500)
        oImage = QImage("./img/img2.jpg")
        sImage = oImage.scaled(QSize(600,400))           
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))                        
        self.setPalette(palette)


        menubar = self.menuBar()
        homeMenu = menubar.addMenu('Home')
        toolMenu = menubar.addMenu('Tools')
        helpMenu = menubar.addMenu('Help')
        
        impMenu = QMenu('Import', self)
        impAct = QAction('Import mail', self)
        impMenu.addAction(impAct)

        newAct = QAction('New', self)

        homeMenu.addAction(newAct)
        homeMenu.addMenu(impMenu)

        self.setWindowTitle('App Truyện')
        self.setWindowIcon(QIcon('./img/icon.jpg'))
        self.show()  