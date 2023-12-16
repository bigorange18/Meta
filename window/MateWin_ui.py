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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QListWidget, QListWidgetItem,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)
import source_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1080, 871)
        icon = QIcon()
        icon.addFile(u"C:/Users/Administrator/.designer/backup/icon/Mate.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QListView {\n"
"\n"
"}\n"
"QListView::item{\n"
"background-color: transparent;\n"
"	color: rgba(255, 255, 255, 199);\n"
"padding:12px;\n"
"padding-left:18px;\n"
"}\n"
"QListView::item:hover {\n"
"	background-color: rgba(175, 139, 255, 59);\n"
"\n"
"}\n"
"QListView::item:selected {\n"
"background-color: rgba(175, 139, 255, 159);\n"
"	color: rgb(255, 255, 255);\n"
"border-left:5px solid rgb(172, 154, 233)\n"
"}\n"
"\n"
"QFrame{\n"
"	background-color: rgb(245, 249, 254);\n"
"border:0px solid red;\n"
"border-radius:30px\n"
"}\n"
"\n"
"rgb(185, 234, 255)")
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
        self.centralwidget.setMinimumSize(QSize(1080, 850))
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(1200, 820))
        self.frame_3.setStyleSheet(u"QFrame#frame{\n"
"	background-color: qlineargradient(x0:0, y1:0,x0:1, y2:1, stop:0 rgb(20, 32, 44), stop:1 rgb(37, 85, 117));\n"
"border-radius:10px  \n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(800, 800))
        self.frame_2.setMaximumSize(QSize(800, 800))
        self.frame_2.setStyleSheet(u"QFrame#frame{\n"
"	background-color: qlineargradient(x0:0, y1:0,x0:1, y2:1, stop:0 rgb(20, 32, 44), stop:1 rgb(37, 85, 117));\n"
"border-radius:20px  \n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.stackedWidget = QStackedWidget(self.frame_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(245, 249, 254);\n"
"border:0px solid red;\n"
"border-radius:30px\n"
"}")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setStyleSheet(u"QFrame#frame{\n"
"	background-color: qlineargradient(x0:0, y1:0,x0:1, y2:1, stop:0 rgb(20, 32, 44), stop:1 rgb(37, 85, 117));\n"
"border-radius:20px  \n"
"}\n"
"\n"
"QWidget {background-color: }")
        self.gridLayout_2 = QGridLayout(self.page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_7, 2, 1, 1, 1)

        self.g_functions = QGroupBox(self.page)
        self.g_functions.setObjectName(u"g_functions")
        self.g_functions.setMinimumSize(QSize(0, 700))
        self.g_functions.setMaximumSize(QSize(16777215, 700))
        self.g_functions.setAlignment(Qt.AlignCenter)
        self.verticalLayout_3 = QVBoxLayout(self.g_functions)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer = QSpacerItem(20, 152, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.b_dectect = QPushButton(self.g_functions)
        self.b_dectect.setObjectName(u"b_dectect")

        self.verticalLayout_3.addWidget(self.b_dectect)

        self.verticalSpacer_2 = QSpacerItem(20, 153, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.b_segmentation = QPushButton(self.g_functions)
        self.b_segmentation.setObjectName(u"b_segmentation")

        self.verticalLayout_3.addWidget(self.b_segmentation)

        self.verticalSpacer_3 = QSpacerItem(20, 152, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.b_filter = QPushButton(self.g_functions)
        self.b_filter.setObjectName(u"b_filter")

        self.verticalLayout_3.addWidget(self.b_filter)

        self.verticalSpacer_4 = QSpacerItem(20, 152, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)


        self.gridLayout_2.addWidget(self.g_functions, 0, 0, 5, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(self.page)
        self.groupBox.setObjectName(u"groupBox")
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

        self.verticalLayout_2.addWidget(self.groupBox)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 3, 1, 2, 1)

        self.horizontalSpacer = QSpacerItem(14, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 4, 2, 1, 1)

        self.lab_img = QLabel(self.page)
        self.lab_img.setObjectName(u"lab_img")
        self.lab_img.setMinimumSize(QSize(640, 480))
        self.lab_img.setMaximumSize(QSize(640, 480))
        self.lab_img.setText(u"")
        self.lab_img.setPixmap(QPixmap(u"D:/Backup/Documents/My Pictures/test1.jpg"))
        self.lab_img.setScaledContents(True)
        self.lab_img.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lab_img, 0, 1, 1, 1)

        self.label_4 = QLabel(self.page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 100))
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_4, 1, 1, 1, 1)

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

        self.horizontalLayout_2.addWidget(self.stackedWidget)


        self.gridLayout_3.addWidget(self.frame_2, 0, 1, 1, 1)

        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(200, 800))
        self.frame.setMaximumSize(QSize(200, 800))
        self.frame.setStyleSheet(u"QFrame#frame{\n"
"	background-color: qlineargradient(x0:0, y1:0,x0:1, y2:1, stop:0 rgb(20, 32, 44), stop:1 rgb(37, 85, 117));\n"
"border-radius:20px  \n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"image:url(:/icon/icon/logo.jpg)")
        self.label_3.setWordWrap(False)

        self.verticalLayout.addWidget(self.label_3)

        self.verticalSpacer_5 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.listWidget = QListWidget(self.frame)
        icon4 = QIcon()
        icon4.addFile(u":/icon/icon/home.png", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem = QListWidgetItem(self.listWidget)
        __qlistwidgetitem.setIcon(icon4);
        icon5 = QIcon()
        icon5.addFile(u":/icon/icon/chat.png", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem1 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem1.setIcon(icon5);
        icon6 = QIcon()
        icon6.addFile(u":/icon/icon/function.png", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem2 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem2.setIcon(icon6);
        icon7 = QIcon()
        icon7.addFile(u":/icon/icon/test.png", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem3 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem3.setIcon(icon7);
        icon8 = QIcon()
        icon8.addFile(u":/icon/icon/win1.png", QSize(), QIcon.Normal, QIcon.Off)
        __qlistwidgetitem4 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem4.setIcon(icon8);
        self.listWidget.setObjectName(u"listWidget")
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

        self.verticalLayout.addWidget(self.listWidget)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"padding:8px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(43, 162, 239);\n"
"	border-radius:24px;\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.pushButton)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_8)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(2, 2)
        self.verticalLayout.setStretch(4, 1)

        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_3, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1080, 21))
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
        self.b_dectect.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u6807\u68c0\u6d4b", None))
        self.b_segmentation.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u6807\u5206\u5272", None))
        self.b_filter.setText(QCoreApplication.translate("MainWindow", u"\u6ee4\u6ce2\u7b97\u6cd5", None))
        self.groupBox.setTitle("")
        self.lab_file_name.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u540d:", None))
        self.b_filename.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6", None))
        self.b_start.setText(QCoreApplication.translate("MainWindow", u"start", None))
        self.b_end.setText(QCoreApplication.translate("MainWindow", u"end", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5370\u8f93\u51fa\u4fe1\u606f", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u53d1\u4e2d", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"111", None))
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
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u6743\u91cd", None))
        self.menu_4.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
    # retranslateUi

