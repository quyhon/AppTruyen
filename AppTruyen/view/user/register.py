import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QImage, QPalette, QBrush, QIcon, QFont

def signUpGUI(self):
    self.signUpLayout = QGridLayout()

    registerLabel = QLabel('     REGISTER')
    nameLabel = QLabel('Name:     ')
    sexLabel =  QLabel('Sex:      ')
    userLabel = QLabel('Username: ')
    passLabel = QLabel('Password: ')

    registerLabel.setStyleSheet("font-size:16pt; font-weight:500; color: rgb(255, 255, 0);")
    nameLabel.setStyleSheet("font-size:12pt; font-weight:400; color: rgb(255,255,0);")
    sexLabel.setStyleSheet("font-size:12pt; font-weight:400; color: rgb(255,255,0);")
    userLabel.setStyleSheet("font-size:12pt; font-weight:400; color: rgb(255,255,0);")
    passLabel.setStyleSheet("font-size:12pt; font-weight:400; color: rgb(255,255,0);")

    self.userEdit = QLineEdit()
    self.passEdit = QLineEdit()
    self.nameEdit = QLineEdit()
    self.sexEdit = QLineEdit()
    self.passEdit.setEchoMode(QtWidgets.QLineEdit.Password)

    self.userEdit.setStyleSheet("border-radius: 5px;")
    self.passEdit.setStyleSheet("border-radius: 5px;")
    self.sexEdit.setStyleSheet("border-radius: 5px;")
    self.nameEdit.setStyleSheet("border-radius: 5px;")

    backSignInButton = QPushButton("Have account?")
    signUpButton = QPushButton("Sign Up")
    backSignInButton.setStyleSheet("border-radius: 5px; background-color: rgb(205, 133, 63); font-size:12pt; font-weight:500;")
    signUpButton.setStyleSheet("border-radius: 5px; background-color: rgb(205, 133, 63); font-size:12pt; font-weight:500;")
    
    backSignInButton.setSizePolicy( QSizePolicy.Expanding, QSizePolicy.Expanding)
    signUpButton.setSizePolicy( QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.userEdit.setSizePolicy( QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.passEdit.setSizePolicy( QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.sexEdit.setSizePolicy( QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.nameEdit.setSizePolicy( QSizePolicy.Expanding, QSizePolicy.Expanding)

    self.signUpLayout.setRowStretch(0,2)
    self.signUpLayout.setRowStretch(1,1)
    self.signUpLayout.setRowStretch(2,1)
    self.signUpLayout.setRowStretch(3,1)
    self.signUpLayout.setRowStretch(4,1)
    self.signUpLayout.setRowStretch(5,1) 
    self.signUpLayout.setRowStretch(6,1) 
    self.signUpLayout.setRowStretch(7,3)

    self.signUpLayout.setColumnStretch(0,1)
    self.signUpLayout.setColumnStretch(1,2)
    self.signUpLayout.setColumnStretch(2,2)
    self.signUpLayout.setColumnStretch(3,2)
    self.signUpLayout.setColumnStretch(4,1)

    
    self.signUpLayout.addWidget(registerLabel,0,2,1,1)
    self.signUpLayout.setSpacing(40)
    font = QFont()
    font.setPointSize(14)
    self.nameEdit.setFont(font)
    self.sexEdit.setFont(font)
    self.userEdit.setFont(font)
    self.passEdit.setFont(font)

    self.signUpLayout.addWidget(nameLabel,1,1,1,1)
    self.signUpLayout.addWidget(self.nameEdit,1,2,1,2)
    self.signUpLayout.setSpacing(10)
    self.signUpLayout.addWidget(sexLabel,2,1,1,1)
    self.signUpLayout.addWidget(self.sexEdit,2,2,1,2)
    self.signUpLayout.addWidget(userLabel,3,1,1,1)
    self.signUpLayout.addWidget(self.userEdit,3,2,1,2)
    self.signUpLayout.addWidget(passLabel,4,1,1,1)
    self.signUpLayout.addWidget(self.passEdit,4,2,1,2)

    self.signUpLayout.addWidget(backSignInButton,6,1,1,1)
    self.signUpLayout.addWidget(signUpButton,6,3,1,1)

    backSignInButton.clicked.connect(self.backSignInEvent)
    signUpButton.clicked.connect(self.registerEvent)

    self.rootLayout.removeItem(self.signInLayout)
    self.clearLayout(self.signInLayout)
    self.rootLayout.addLayout(self.signUpLayout)