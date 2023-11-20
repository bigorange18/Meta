


# 导入sys
import sys

# 任何一个PySide界面程序都需要使用QApplication
# 我们要展示一个普通的窗口，所以需要导入QWidget，用来让我们自己的类继承
from PySide6.QtWidgets import QApplication, QWidget,QMessageBox
from PySide6.QtWidgets import QMainWindow, QDialog, QLabel, QPushButton, QLineEdit
from PySide6.QtGui import QCursor
from PySide6.QtCore import Qt
# 导入我们生成的界面
from untitled_ui import Ui_Dialog
 
import qtmodern.styles
from qtmodern import styles, windows

# 继承QWidget类，以获取其属性和方法
class MainWindow(QWidget, Ui_Dialog):
    def __init__(self, win_width=500):
        super().__init__()
        # 设置窗口标题
        self.setWindowTitle("登录界面")
        # 设置窗口大小
        self.setFixedSize(win_width, int(win_width*0.75))
        # 调整窗口位置
        qr = self.frameGeometry()
        screen_w = QApplication.primaryScreen().size().width()
        screen_h = QApplication.primaryScreen().size().height()
        w_x = (screen_w - win_width) / 2
        w_y = (screen_h - win_width*0.75) / 2
        self.move(w_x, w_y)


        # self.move(1000, 200)
        # 
        # self.setStyleSheet("background: rgb(132, 189, 179);")

        # 设置界面为我们生成的界面
        self.setupUi(self)

        # 给登录按钮增加属性
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(
            "*{border: 4px solid '#BC006C;" +
            "border-radius: 45px;" +
            "font-size: 35px;" + 
            "color: 'white';" + 
            "padding: 25px 0;" + 
            "margin: 100px 200px;}" +
            "*:hover{background: '#BC006C'};")
        # self.pushButton.clicked.connect(self.on_botton_clicked)
        # self.show()

    def on_botton_clicked(self):
        msg = QMessageBox.clickedButton(QMessageBox(), "提示确定")
        print("button clicked")

# 程序入口
if __name__ == "__main__":
    # 初始化QApplication，界面展示要包含在QApplication初始化之后，结束之前
    app = QApplication(sys.argv)
    
    # qtmodern.styles.dark(app)
    # 初始化并展示我们的界面组件
    window = MainWindow()
    # window.show()
    # win = qtmodern.windows.ModernWindow(window)
    window.show() 
    # 结束QApplication
    sys.exit(app.exec_())
