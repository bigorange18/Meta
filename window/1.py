# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
# from PyQt5.uic import loadUi
# from login_ui import Ui_Dialog

# class LoginWindow(QWidget):

#     '''登录窗口'''
#     def __init__(self, parent=None):
#         super().__init__()

#         loadUi('login.ui', self)  # 将my_ui.ui文件加载到window对象中
#         # self.setupUi(self)
#         self.show()
#         pass

# class MateWindow(QMainWindow):
#     '''Meta处理窗口'''
#     def __init__(self, parent=None):
#         super().__init__()
#         loadUi('MateWin.ui', self)  # 将my_ui.ui文件加载到window对象中
#         self.show()
#         pass


# # 程序入口
# if __name__ == "__main__":
#     # 初始化QApplication，界面展示要包含在QApplication初始化之后，结束之前
#     app = QApplication(sys.argv)
#     window = MateWindow()
#     sys.exit(app.exec_())

import sys
 
from play_ui import *
from PySide6.QtCore import QUrl
from PySide6.QtMultimedia import QAudioOutput, QMediaPlayer
from PySide6.QtWidgets import QMainWindow, QApplication
 
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5 import uic
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._audio_output = QAudioOutput()
        self._player = QMediaPlayer()
        self._player.setAudioOutput(self._audio_output)
        self._player.setVideoOutput(self.ui._video_widget)
 

    def loadVideo(self):
        


        # 播放视频
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.vw) # 视频播放的widget
        self.player.setMedia(QMediaContent(QFileDialog.getOpenFileUrl()[0])) # 选取视频文件

 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.setWindowTitle("Min_Player")
    main_win.show()
    main_win.play()
    sys.exit(app.exec())