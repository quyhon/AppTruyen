from PyQt5.QtWidgets import QMessageBox

def showMessage(self,tilte,messageStr):
    """Show message"""
    QMessageBox.information(self,tilte,messageStr)