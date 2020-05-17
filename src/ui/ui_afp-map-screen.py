# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'afp-map-screenKrYpsO.ui'
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


class Ui_AccessMapScreen(object):
    def setupUi(self, AccessMapScreen):
        if not AccessMapScreen.objectName():
            AccessMapScreen.setObjectName(u"AccessMapScreen")
        AccessMapScreen.resize(400, 300)
        self.verticalLayout_2 = QVBoxLayout(AccessMapScreen)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.checkBox_3 = QCheckBox(AccessMapScreen)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.horizontalLayout.addWidget(self.checkBox_3)

        self.checkBox = QCheckBox(AccessMapScreen)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(AccessMapScreen)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.horizontalLayout.addWidget(self.checkBox_2)


        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.widget = QWidget(AccessMapScreen)
        self.widget.setObjectName(u"widget")

        self.gridLayout_2.addWidget(self.widget, 0, 0, 2, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)


        self.retranslateUi(AccessMapScreen)

        QMetaObject.connectSlotsByName(AccessMapScreen)
    # setupUi

    def retranslateUi(self, AccessMapScreen):
        AccessMapScreen.setWindowTitle(QCoreApplication.translate("AccessMapScreen", u"Form", None))
        self.checkBox_3.setText(QCoreApplication.translate("AccessMapScreen", u"\u0395\u03bc\u03c0\u03cc\u03b4\u03b9\u03b1", None))
        self.checkBox.setText(QCoreApplication.translate("AccessMapScreen", u"\u03a4\u03bf\u03c5\u03b1\u03bb\u03ad\u03c4\u03b5\u03c2", None))
        self.checkBox_2.setText(QCoreApplication.translate("AccessMapScreen", u"\u03a0\u03ac\u03c1\u03ba\u03b9\u03bd\u03b3\u03ba", None))
    # retranslateUi

