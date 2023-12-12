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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QWidget)

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
        self.a_Exit = QAction(MainWindow)
        self.a_Exit.setObjectName(u"a_Exit")
        icon3 = QIcon()
        icon3.addFile(u"C:/Users/Administrator/.designer/backup/icon/exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.a_Exit.setIcon(icon3)
        self.a_file = QAction(MainWindow)
        self.a_file.setObjectName(u"a_file")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.g_functions = QGroupBox(self.centralwidget)
        self.g_functions.setObjectName(u"g_functions")
        self.g_functions.setGeometry(QRect(30, 70, 205, 761))
        self.g_functions.setAlignment(Qt.AlignCenter)
        self.gridLayout = QGridLayout(self.g_functions)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 152, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(46, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 2)

        self.horizontalSpacer_2 = QSpacerItem(46, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 3, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 153, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(46, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 3, 0, 1, 2)

        self.b_segmentation = QPushButton(self.g_functions)
        self.b_segmentation.setObjectName(u"b_segmentation")

        self.gridLayout.addWidget(self.b_segmentation, 3, 2, 1, 2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 3, 4, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 152, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 4, 2, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 5, 0, 1, 1)

        self.b_filter = QPushButton(self.g_functions)
        self.b_filter.setObjectName(u"b_filter")

        self.gridLayout.addWidget(self.b_filter, 5, 1, 1, 2)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 5, 4, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 152, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 6, 2, 1, 1)

        self.b_dectect = QPushButton(self.g_functions)
        self.b_dectect.setObjectName(u"b_dectect")

        self.gridLayout.addWidget(self.b_dectect, 1, 2, 1, 1)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(300, 60, 1281, 781))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.lab_img = QLabel(self.page)
        self.lab_img.setObjectName(u"lab_img")
        self.lab_img.setGeometry(QRect(50, 70, 640, 480))
        self.lab_img.setMinimumSize(QSize(640, 480))
        self.lab_img.setPixmap(QPixmap(u"D:/Backup/Documents/My Pictures/test1.jpg"))
        self.lab_img.setScaledContents(True)
        self.lab_img.setAlignment(Qt.AlignCenter)
        self.groupBox = QGroupBox(self.page)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(60, 680, 631, 58))
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lab_file_name = QLabel(self.groupBox)
        self.lab_file_name.setObjectName(u"lab_file_name")
        self.lab_file_name.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lab_file_name)

        self.b_filename = QPushButton(self.groupBox)
        self.b_filename.setObjectName(u"b_filename")

        self.horizontalLayout.addWidget(self.b_filename)

        self.b_start = QPushButton(self.groupBox)
        self.b_start.setObjectName(u"b_start")

        self.horizontalLayout.addWidget(self.b_start)

        self.horizontalLayout.setStretch(1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label = QLabel(self.page_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(490, 400, 53, 15))
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label_2 = QLabel(self.page_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(400, 360, 53, 15))
        self.stackedWidget.addWidget(self.page_3)
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

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menu.addAction(self.a_file)
        self.menu.addAction(self.a_Exit)
        self.menu_2.addAction(self.stresstest)
        self.menu_4.addAction(self.version)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MateWin", None))
        self.stresstest.setText(QCoreApplication.translate("MainWindow", u"\u538b\u529b\u6d4b\u8bd5", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"\u8f6f\u4ef6\u7248\u672c", None))
        self.a_Exit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.a_file.setText(QCoreApplication.translate("MainWindow", u"\u6700\u8fd1\u6587\u4ef6", None))
        self.g_functions.setTitle(QCoreApplication.translate("MainWindow", u"\u529f\u80fd\u533a", None))
        self.b_segmentation.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u6807\u5206\u5272", None))
        self.b_filter.setText(QCoreApplication.translate("MainWindow", u"\u6ee4\u6ce2\u7b97\u6cd5", None))
        self.b_dectect.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u6807\u68c0\u6d4b", None))
        self.lab_img.setText("")
        self.groupBox.setTitle("")
        self.lab_file_name.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u540d:", None))
        self.b_filename.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6", None))
        self.b_start.setText(QCoreApplication.translate("MainWindow", u"start", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u53d1\u4e2d", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"111", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u6d4b\u8bd5", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u5206\u6790", None))
        self.menu_4.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
    # retranslateUi

