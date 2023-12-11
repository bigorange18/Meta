# -*- coding: utf-8 -*-
 
################################################################################
## Form generated from reading UI file 'playerhHhzqy.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import (QApplication, QMainWindow, QSizePolicy, QWidget)
 
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(798, 601)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self._video_widget = QVideoWidget(self.centralwidget)
        self._video_widget.setObjectName(u"_video_widget")
        self._video_widget.setGeometry(QRect(0, 0, 821, 621))
        MainWindow.setCentralWidget(self.centralwidget)
 
        self.retranslateUi(MainWindow)
 
        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi
 
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
    # retranslateUi
 