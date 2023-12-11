import sys
import cv2
from PySide6.QtWidgets import QApplication, QWidget,QMessageBox,QMainWindow,QFileDialog,QDialog,QScrollArea,QLabel
from PySide6.QtWidgets import QMainWindow, QDialog, QLabel, QPushButton, QLineEdit
from PySide6.QtGui import QCursor, QPixmap
from PySide6.QtCore import Qt
from PySide6.QtUiTools import QUiLoader
from window.login_ui import Ui_Dialog
from window.MateWin_ui import Ui_MainWindow
from lib.Windows import Windows

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
        #! todo
        msg = QMessageBox.clickedButton(QMessageBox())
        username = self.login_name.text().strip()
        password = self.login_password.text().strip()
        print(username, password)
        print("button clicked")
        # 关闭当前页面,打开Meta处理界面
        Windows.MetaWin = MateWindow()
        Windows.MetaWin.show()
        self.hide()
        # 清空密码
        self.login_password.setText("")


    def loadVideo(self):
        # self.player.setMedia(QMediaContent(QFileDialog.getOpenFileUrl()[0])) # 选取视频文件
        pass



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
        self.win_x = (screen_w/2 - win_w)
        self.win_y = (screen_h/2 - win_h) 
        self.move(self.win_x, self.win_y)
        self.setupUi(self)
        print(self.file_show.size())
        self.msg_1 = []
        self.button_filename.clicked.connect(self.select_file)
        self.show()

    def back2login(self):
        print("button clicked")
        self.close()
        # Windows.LoginWin.show()


    def msg_print(self):
        for i in range(100):
            self.msg_1.append(1)
        print(self.msg_1)
        self.label.setText(str(self.msg_1))
        self.label.repaint()

    def palyvideo(self):
        pass


    def select_file(self):
        self.file_path, _ = QFileDialog.getOpenFileName(self,dir="./Mate/img", filter="*.jpg; *.png; *.jpeg")
        if self.file_path:
            self.file_show.setPixmap(QPixmap(self.file_path))
            self.file_name.setText(self.file_path)


# 程序入口
if __name__ == "__main__":
    # 初始化QApplication，界面展示要包含在QApplication初始化之后，结束之前
    app = QApplication(sys.argv)
    
    # qtmodern.styles.dark(app)
    # 初始化并展示我们的界面组件
    Windows.LoginWin = MateWindow()
    Windows.LoginWin.show() 
    # 结束QApplication
    sys.exit(app.exec())
    
