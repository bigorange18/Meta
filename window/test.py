import sys
from PySide6.QtWidgets import QApplication, QWidget,QMessageBox,QMainWindow,QFileDialog,QDialog
from PySide6.QtWidgets import QMainWindow, QDialog, QLabel, QPushButton, QLineEdit
from PySide6.QtGui import QCursor
from PySide6.QtCore import Qt
from PySide6.QtUiTools import QUiLoader
from login_ui import Ui_Dialog
from MateWin_ui import Ui_MainWindow
from all_win import Wins

# 继承QWidget类，以获取其属性和方法
class LoginWindow(QWidget, Ui_Dialog):
    '''登录界面处理窗口'''
    def __init__(self, win_width=500):
        super().__init__()
        # 设置窗口标题
        self.setWindowTitle("登录界面")
        # 调整窗口位置
        qr = self.frameGeometry()
        screen_w = QApplication.primaryScreen().size().width()
        screen_h = QApplication.primaryScreen().size().height()
        win_w = self.frameGeometry().getRect()[2]
        win_h = self.frameGeometry().getRect()[3]
        self.win_x = (screen_w - win_w) / 2
        self.win_y = (screen_h - win_h) / 2
        self.move(self.win_x, self.win_y)
        self.setupUi(self)
        # 登录
        self.login_button.clicked.connect(self.login_botton_clicked)
        # 取消
        self.login_fail.clicked.connect(self.closewin)

    def login_botton_clicked(self):
        msg = QMessageBox.clickedButton(QMessageBox())
        username = self.login_name.text().strip()
        password = self.login_password.text().strip()
        print(username, password)
        print("button clicked")
        # 关闭当前页面,打开Meta处理界面
        Wins.MetaWin = MateWindow()
        Wins.MetaWin.show()
        self.hide()
        # 清空密码
        self.login_password.setText("")

    def closewin(self):
        return self.close()



class MateWindow(QMainWindow,Ui_MainWindow):
    '''Meta处理窗口'''
    def __init__(self, parent=None):
        super().__init__()
        screen_w = QApplication.primaryScreen().size().width()
        screen_h = QApplication.primaryScreen().size().height()
        win_w = self.frameGeometry().getRect()[2]
        win_h = self.frameGeometry().getRect()[3]
        self.win_x = (screen_w - win_w) / 2
        self.win_y = (screen_h - win_h) / 2
        self.move(self.win_x, self.win_y)
        self.setupUi(self)
        self.actionExit.triggered.connect(self.back2login)
        self.show()

    def back2login(self):
        print("button clicked")
        self.close()
        Wins.LoginWin.show()



# 程序入口
if __name__ == "__main__":
    # 初始化QApplication，界面展示要包含在QApplication初始化之后，结束之前
    app = QApplication(sys.argv)
    
    # qtmodern.styles.dark(app)
    # 初始化并展示我们的界面组件
    Wins.LoginWin = LoginWindow()
    Wins.LoginWin.show() 
    # 结束QApplication
    sys.exit(app.exec())
    
