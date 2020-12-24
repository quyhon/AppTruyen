import sys
from PyQt5.QtWidgets import QApplication

def main():
    app = QApplication(sys.argv)
    import view.user.index as index
    si = index.Main()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()