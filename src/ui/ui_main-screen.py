# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main-screeniyKNOS.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainScreen(object):
    def setupUi(self, MainScreen):
        if not MainScreen.objectName():
            MainScreen.setObjectName(u"MainScreen")
        MainScreen.resize(400, 296)
        self.verticalLayout_2 = QVBoxLayout(MainScreen)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_2 = QPushButton(MainScreen)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(MainScreen)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(MainScreen)

        QMetaObject.connectSlotsByName(MainScreen)
    # setupUi

    def retranslateUi(self, MainScreen):
        MainScreen.setWindowTitle(QCoreApplication.translate("MainScreen", u"Form", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainScreen", u"\u03a7\u03ac\u03c1\u03c4\u03b7\u03c2 \u03a0\u03c1\u03cc\u03c3\u03b2\u03b1\u03c3\u03b7\u03c2", None))
        self.pushButton.setText(QCoreApplication.translate("MainScreen", u"\u0391\u03bd\u03b1\u03c6\u03bf\u03c1\u03ac \u03a0\u03c1\u03bf\u03b2\u03bb\u03ae\u03bc\u03b1\u03c4\u03bf\u03c2", None))
    # retranslateUi

