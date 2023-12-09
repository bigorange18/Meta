import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.uic import loadUi
from login_ui import Ui_Dialog

class LoginWindow(QWidget):

    '''登录窗口'''
    def __init__(self, parent=None):
        super().__init__()
        loadUi('login.ui', self)  # 将my_ui.ui文件加载到window对象中
        # self.setupUi(self)
        self.show()
        pass

class MateWindow(QMainWindow):
    '''Meta处理窗口'''
    def __init__(self, parent=None):
        super().__init__()
        loadUi('MateWin.ui', self)  # 将my_ui.ui文件加载到window对象中
        self.show()
        pass


# 程序入口
if __name__ == "__main__":
    # 初始化QApplication，界面展示要包含在QApplication初始化之后，结束之前
    app = QApplication(sys.argv)
    window = MateWindow()
    sys.exit(app.exec_())