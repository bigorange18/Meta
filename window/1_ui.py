# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '1.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QListWidget, QListWidgetItem,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QWidget)
import source_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(360, 60, 121, 751))
        self.frame.setStyleSheet(u"QFrame#frame{\n"
"	background-color: qlineargradient(x0:0, y1:0,x0:1, y2:1, stop:0 rgb(20, 32, 44), stop:1 rgb(37, 85, 117));\n"
"border-radius:20px  \n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 30, 111, 51))
        self.label_3.setStyleSheet(u"image:url(:/icon/icon/logo.jpg)")
        self.label_3.setWordWrap(False)
        self.listWidget = QListWidget(self.frame)
        icon = QIcon()
        icon.addFile(u":/icon/icon/home.png", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem = QListWidgetItem(self.listWidget)
        __qlistwidgetitem.setIcon(icon);
        icon1 = QIcon()
        icon1.addFile(u":/icon/icon/chat.png", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem1 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem1.setIcon(icon1);
        icon2 = QIcon()
        icon2.addFile(u":/icon/icon/function.png", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem2 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem2.setIcon(icon2);
        icon3 = QIcon()
        icon3.addFile(u":/icon/icon/test.png", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem3 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem3.setIcon(icon3);
        icon4 = QIcon()
        icon4.addFile(u":/icon/icon/win1.png", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem4 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem4.setIcon(icon4);
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(0, 220, 91, 321))
        self.listWidget.setStyleSheet(u"QListView {\n"
"	border:none;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QListView::item{\n"
"background-color: transparent;\n"
"height:40px;\n"
"padding-left:4px;\n"
"\n"
"}\n"
"QListView::item:hover {\n"
"	background-color:  transparent;\n"
"	color: rgba(43, 162, 238,150);\n"
"\n"
"}\n"
"QListView::item:selected {\n"
"	/*background-color: transparent;*/\n"
"background-color:  transparent;\n"
"	color: rgb(43, 162, 238);\n"
"}\n"
"")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 680, 91, 41))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"padding:8px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(43, 162, 239);\n"
"	border-radius:16px;\n"
"}\n"
"")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(490, 70, 861, 751))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.stackedWidget = QStackedWidget(self.frame_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 40, 841, 701))
        self.stackedWidget.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(245, 249, 254);\n"
"border:0px solid red;\n"
"border-radius:30px\n"
"}")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.lab_img = QLabel(self.page)
        self.lab_img.setObjectName(u"lab_img")
        self.lab_img.setGeometry(QRect(180, 40, 640, 480))
        self.lab_img.setMinimumSize(QSize(640, 480))
        self.lab_img.setText(u"")
        self.lab_img.setPixmap(QPixmap(u"D:/Backup/Documents/My Pictures/test1.jpg"))
        self.lab_img.setScaledContents(True)
        self.lab_img.setAlignment(Qt.AlignCenter)
        self.groupBox = QGroupBox(self.page)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(200, 620, 621, 58))
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

        self.b_end = QPushButton(self.groupBox)
        self.b_end.setObjectName(u"b_end")

        self.horizontalLayout.addWidget(self.b_end)

        self.horizontalLayout.setStretch(1, 1)
        self.label_4 = QLabel(self.page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(200, 550, 601, 61))
        self.label_4.setAlignment(Qt.AlignCenter)
        self.g_functions = QGroupBox(self.page)
        self.g_functions.setObjectName(u"g_functions")
        self.g_functions.setGeometry(QRect(20, 110, 101, 411))
        self.g_functions.setAlignment(Qt.AlignCenter)
        self.gridLayout = QGridLayout(self.g_functions)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 3, 4, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 152, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 4, 2, 1, 1)

        self.b_dectect = QPushButton(self.g_functions)
        self.b_dectect.setObjectName(u"b_dectect")

        self.gridLayout.addWidget(self.b_dectect, 1, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 153, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 2, 1, 1)

        self.b_segmentation = QPushButton(self.g_functions)
        self.b_segmentation.setObjectName(u"b_segmentation")

        self.gridLayout.addWidget(self.b_segmentation, 3, 2, 1, 2)

        self.b_filter = QPushButton(self.g_functions)
        self.b_filter.setObjectName(u"b_filter")

        self.gridLayout.addWidget(self.b_filter, 5, 1, 1, 2)

        self.horizontalSpacer_2 = QSpacerItem(46, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 3, 1, 2)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 5, 0, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 5, 4, 1, 1)

        self.horizontalSpacer = QSpacerItem(46, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 2)

        self.horizontalSpacer_3 = QSpacerItem(46, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 3, 0, 1, 2)

        self.verticalSpacer_4 = QSpacerItem(20, 152, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 6, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 152, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 2, 1, 1)

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
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText("")

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Home", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Chatgpt", None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u529f\u80fd", None));
        ___qlistwidgetitem3 = self.listWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u535a\u5ba2", None));
        ___qlistwidgetitem4 = self.listWidget.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u5176\u4ed6", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u4e2a\u4eba\u4fe1\u606f", None))
        self.groupBox.setTitle("")
        self.lab_file_name.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u540d:", None))
        self.b_filename.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6", None))
        self.b_start.setText(QCoreApplication.translate("MainWindow", u"start", None))
        self.b_end.setText(QCoreApplication.translate("MainWindow", u"end", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5370\u8f93\u51fa\u4fe1\u606f", None))
        self.g_functions.setTitle(QCoreApplication.translate("MainWindow", u"\u529f\u80fd\u533a", None))
        self.b_dectect.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u6807\u68c0\u6d4b", None))
        self.b_segmentation.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u6807\u5206\u5272", None))
        self.b_filter.setText(QCoreApplication.translate("MainWindow", u"\u6ee4\u6ce2\u7b97\u6cd5", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u53d1\u4e2d", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"111", None))
    # retranslateUi

