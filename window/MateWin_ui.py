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
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QLabel, QListView,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QToolBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        icon = QIcon()
        icon.addFile(u"C:/Users/Administrator/.designer/backup/icon/win1.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolButtonStyle(Qt.ToolButtonTextOnly)
        self.stresstest = QAction(MainWindow)
        self.stresstest.setObjectName(u"stresstest")
        icon1 = QIcon()
        icon1.addFile(u"C:/Users/Administrator/.designer/backup/icon/\u538b\u529b\u6d4b\u8bd5.png", QSize(), QIcon.Normal, QIcon.Off)
        self.stresstest.setIcon(icon1)
        self.version = QAction(MainWindow)
        self.version.setObjectName(u"version")
        icon2 = QIcon()
        icon2.addFile(u"C:/Users/Administrator/.designer/backup/icon/\u5b98\u65b9\u7248\u672c.png", QSize(), QIcon.Normal, QIcon.Off)
        self.version.setIcon(icon2)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        icon3 = QIcon()
        icon3.addFile(u"C:/Users/Administrator/.designer/backup/icon/\u9000\u51fa.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionExit.setIcon(icon3)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.funcion = QListView(self.centralwidget)
        self.funcion.setObjectName(u"funcion")
        self.funcion.setGeometry(QRect(10, 10, 221, 491))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 20, 101, 16))
        self.label.setAlignment(Qt.AlignCenter)
        self.dateTimeEdit = QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setGeometry(QRect(600, 0, 194, 22))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(70, 150, 75, 23))
        self.pushButton_1 = QPushButton(self.centralwidget)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setGeometry(QRect(70, 90, 75, 23))
        self.label_show = QLabel(self.centralwidget)
        self.label_show.setObjectName(u"label_show")
        self.label_show.setGeometry(QRect(330, 60, 261, 51))
        self.label_show.setWordWrap(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        self.menu_4 = QMenu(self.menubar)
        self.menu_4.setObjectName(u"menu_4")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
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
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u529f\u80fd", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u529f\u80fd\u4e8c", None))
        self.pushButton_1.setText(QCoreApplication.translate("MainWindow", u"\u529f\u80fd\u4e00", None))
        self.label_show.setText(QCoreApplication.translate("MainWindow", u"print_show", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u6d4b\u8bd5", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u5206\u6790", None))
        self.menu_4.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

