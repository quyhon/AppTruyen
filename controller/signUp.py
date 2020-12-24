from PyQt5.QtWidgets import QMessageBox
import view.user.register as register
import view.messager as messager
import model.check as check
import model.connectDB as connectDB

def event(self):
    """Event SignUp"""
    reply = QMessageBox.question(self,'Message',"Bạn chưa có tài khoản?", QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
    if reply == QMessageBox.Yes:
        register.signUpGUI(self)
    else:
        pass
def registerEvent(self):
    """Register Event"""
    if check.checkNullRegister(self):
        data = [self.userEdit.text(), self.passEdit.text(), self.nameEdit.text(), self.sexEdit.text()]
        if connectDB.register(data):
            messager.showMessage(self,'Success','Register Success, back to login ?')
            #Back LoginGUI
            self.backSignInEvent()
        else:
            messager.showMessage(self,'Error','Account already exists !')
    else:
        messager.showMessage(self,"Error","Vui lòng điền đủ thông tin!")