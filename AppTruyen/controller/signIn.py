import view.messager as messager
import view.user.login as login
import model.connectDB as connectDB

import view.home.homeGUI as homeGUI
si = homeGUI.home()

def event(self):
    """Event SignIn"""
    if connectDB.checkUser(self.userEdit.text(),self.passEdit.text()):
        messager.showMessage(self,'Success','Đăng nhập thành công!')
        si.homeGUI()
        self.close()
    else:
        messager.showMessage(self,'Err','Đăng nhập không thành công!')
        self.userEdit.setText("")
        self.passEdit.setText("")
def back(self):
    """Back SignIn GUI"""
    self.rootLayout.removeItem(self.signUpLayout)
    self.clearLayout(self.signUpLayout)
    login.signInGUI(self)