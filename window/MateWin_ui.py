# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MateWin.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QToolBar,
    QWidget)
import window.source_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1600, 1000)
        MainWindow.setMinimumSize(QSize(1600, 1000))
        MainWindow.setMaximumSize(QSize(1600, 1000))
        icon = QIcon()
        icon.addFile(u"C:/Users/Administrator/.designer/backup/icon/Mate.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolButtonStyle(Qt.ToolButtonTextOnly)
        self.stresstest = QAction(MainWindow)
        self.stresstest.setObjectName(u"stresstest")
        icon1 = QIcon()
        icon1.addFile(u"C:/Users/Administrator/.designer/backup/icon/test.png", QSize(), QIcon.Normal, QIcon.Off)
        self.stresstest.setIcon(icon1)
        self.version = QAction(MainWindow)
        self.version.setObjectName(u"version")
        icon2 = QIcon()
        icon2.addFile(u"C:/Users/Administrator/.designer/backup/icon/version.png", QSize(), QIcon.Normal, QIcon.Off)
        self.version.setIcon(icon2)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        icon3 = QIcon()
        icon3.addFile(u"C:/Users/Administrator/.designer/backup/icon/exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionExit.setIcon(icon3)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.button_filename = QPushButton(self.centralwidget)
        self.button_filename.setObjectName(u"button_filename")
        self.button_filename.setGeometry(QRect(840, 650, 391, 23))
        self.button_start = QPushButton(self.centralwidget)
        self.button_start.setObjectName(u"button_start")
        self.button_start.setGeometry(QRect(1340, 650, 75, 23))
        self.file_show = QLabel(self.centralwidget)
        self.file_show.setObjectName(u"file_show")
        self.file_show.setGeometry(QRect(720, 60, 640, 480))
        self.file_show.setMinimumSize(QSize(640, 480))
        self.file_show.setPixmap(QPixmap(u"D:/Backup/Documents/My Pictures/test1.jpg"))
        self.file_show.setScaledContents(True)
        self.file_show.setAlignment(Qt.AlignCenter)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(100, 120, 75, 23))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(100, 220, 75, 23))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(100, 390, 75, 23))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(760, 660, 53, 15))
        self.label.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1600, 21))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        self.menu_4 = QMenu(self.menubar)
        self.menu_4.setObjectName(u"menu_4")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menu.addAction(self.stresstest)
        self.menu.addAction(self.actionExit)
        self.menu_2.addAction(self.stresstest)
        self.menu_4.addAction(self.version)
        self.toolBar.addAction(self.stresstest)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MateWin", None))
        self.stresstest.setText(QCoreApplication.translate("MainWindow", u"\u538b\u529b\u6d4b\u8bd5", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"\u8f6f\u4ef6\u7248\u672c", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.button_filename.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6", None))
        self.button_start.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.file_show.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u540d:", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u6d4b\u8bd5", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u5206\u6790", None))
        self.menu_4.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

