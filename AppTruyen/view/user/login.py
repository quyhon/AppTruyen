import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QImage, QPalette, QBrush, QIcon, QFont

def signInGUI(self):
    """đăng nhập GUI"""
    self.signInLayout = QGridLayout()

    loginLabel = QLabel('     LOGIN')
    loginLabel.setStyleSheet("font-size:16pt; font-weight:500; color: rgb(255, 255, 0);")
    userLabel = QLabel('Username: ')
    passLabel = QLabel('Password: ')
    userLabel.setStyleSheet("font-size:12pt; font-weight:400; color: rgb(255,255,0);")
    passLabel.setStyleSheet("font-size:12pt; font-weight:400; color: rgb(255,255,0);")
    self.userEdit = QLineEdit()
    self.passEdit = QLineEdit()
    self.passEdit.setEchoMode(QtWidgets.QLineEdit.Password)
    self.userEdit.setStyleSheet("border-radius: 5px;")
    self.passEdit.setStyleSheet("border-radius: 5px;")
    signInButton = QPushButton("Sign In")
    signUpButton = QPushButton("Sign Up")
    signInButton.setStyleSheet("border-radius: 5px; background-color: rgb(205, 133, 63); font-size:12pt; font-weight:500;")
    signUpButton.setStyleSheet("border-radius: 5px; background-color: rgb(205, 133, 63); font-size:12pt; font-weight:500;")
    signInButton.setSizePolicy( QSizePolicy.Expanding, QSizePolicy.Expanding)
    signUpButton.setSizePolicy( QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.userEdit.setSizePolicy( QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.passEdit.setSizePolicy( QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.signInLayout.setRowStretch(0,2)
    self.signInLayout.setRowStretch(1,1)
    self.signInLayout.setRowStretch(2,1)
    self.signInLayout.setRowStretch(3,1)
    self.signInLayout.setRowStretch(4,1)
    self.signInLayout.setRowStretch(5,5)  
    self.signInLayout.setColumnStretch(0,1)
    self.signInLayout.setColumnStretch(1,2)
    self.signInLayout.setColumnStretch(2,2)
    self.signInLayout.setColumnStretch(3,2)
    self.signInLayout.setColumnStretch(4,1)

    self.signInLayout.addWidget(loginLabel,0,2,1,1)
    self.signInLayout.setSpacing(40)
    font = QFont()
    font.setPointSize(14)
    self.userEdit.setFont(font)
    self.passEdit.setFont(font)
    self.signInLayout.addWidget(userLabel,1,1,1,1)  
    self.signInLayout.addWidget(self.userEdit,1,2,1,2)  
    self.signInLayout.setSpacing(10)
    self.signInLayout.addWidget(passLabel,2,1,1,1)
    self.signInLayout.addWidget(self.passEdit,2,2,1,2)
    self.signInLayout.addWidget(signInButton,4,1)
    self.signInLayout.addWidget(signUpButton,4,3)

    signInButton.clicked.connect(self.signInEvent)
    signUpButton.clicked.connect(self.signUpEvent)

    self.rootLayout.addLayout(self.signInLayout)