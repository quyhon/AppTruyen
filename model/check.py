def checkNullRegister(self):
    """Check data Register"""
    if self.userEdit.text() =='' or self.passEdit.text()=='' or self.nameEdit.text()=='' or self.sexEdit.text()=='':
        return 0
    else:
        return 1