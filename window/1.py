# 0. 导入需要的包和模块
from PyQt5.QtWidgets import *
import sys

class MyLabel(QLabel):
   def __init__(self, *args, **kwargs):
       super(MyLabel, self).__init__(*args, **kwargs)
       self.move(100, 100)
       self.setStyleSheet("font-size: 22px;")

   def setSec(self, sec):
       self.setText(str(sec))

   def startMyTimer(self, ms):
       self.timer_id = self.startTimer(ms)

   def timerEvent(self, *args, **kwargs):
       # 获取当前的标签内容
       current_sec = int(self.text())
       current_sec -= 1
       self.setText(str(current_sec))
       if current_sec == 0:
           self.killTimer(self.timer_id)

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件(创建窗口)
window = QWidget()
# 2.2 设置控件(窗口属性设置)
window.setWindowTitle("QObject定时器的使用")
window.resize(500, 500)

# 设置内部控件
label = MyLabel(window)
# 计时时间
label.setSec(5)
# 计时间隔
label.startMyTimer(500)

# 2.3 展示控件
window.show()
# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
