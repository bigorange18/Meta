# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1009, 547)
        icon = QIcon()
        icon.addFile(u"icon/2.jpg", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout_3 = QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setFamilies([u"\u5b8b\u4f53"])
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setPixmap(QPixmap(u"icon/LOGO.png"))

        self.horizontalLayout_4.addWidget(self.label_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.login_name = QLineEdit(Dialog)
        self.login_name.setObjectName(u"login_name")

        self.horizontalLayout.addWidget(self.login_name)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.login_password = QLineEdit(Dialog)
        self.login_password.setObjectName(u"login_password")
        self.login_password.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_2.addWidget(self.login_password)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.checkBox = QCheckBox(Dialog)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout.addWidget(self.checkBox)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.login_button = QPushButton(Dialog)
        self.login_button.setObjectName(u"login_button")

        self.horizontalLayout_3.addWidget(self.login_button)

        self.login_fail = QPushButton(Dialog)
        self.login_fail.setObjectName(u"login_fail")

        self.horizontalLayout_3.addWidget(self.login_fail)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_4.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 8)

        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"login", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u6b22\u8fce\u767b\u5f55Meta\u7cfb\u7edf\uff01", None))
        self.label_3.setText("")
        self.label.setText(QCoreApplication.translate("Dialog", u"\u7528\u6237\u540d:", None))
        self.login_name.setPlaceholderText(QCoreApplication.translate("Dialog", u"eg:orange", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u5bc6   \u7801:", None))
        self.login_password.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u5bc6\u7801\u957f\u5ea6\u4e0d\u5c0f\u4e8e4\uff01", None))
        self.checkBox.setText(QCoreApplication.translate("Dialog", u"\u8bb0\u4f4f\u5bc6\u7801", None))
        self.login_button.setText(QCoreApplication.translate("Dialog", u"\u767b\u5f55", None))
        self.login_fail.setText(QCoreApplication.translate("Dialog", u"\u53d6\u6d88", None))
    # retranslateUi

