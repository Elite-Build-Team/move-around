# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'access-map-screenOuygyZ.ui'
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

from PySide2.QtQuickWidgets import QQuickWidget



class Ui_AccessMapScreen(object):
    def setupUi(self, AccessMapScreen):
        if not AccessMapScreen.objectName():
            AccessMapScreen.setObjectName(u"AccessMapScreen")
        AccessMapScreen.resize(390, 298)
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
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.quickWidget = QQuickWidget(self.widget)
        self.quickWidget.setObjectName(u"quickWidget")
        self.quickWidget.setResizeMode(QQuickWidget.SizeRootObjectToView)

        self.horizontalLayout_2.addWidget(self.quickWidget)


        self.gridLayout_2.addWidget(self.widget, 0, 0, 2, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)


        self.retranslateUi(AccessMapScreen)

        QMetaObject.connectSlotsByName(AccessMapScreen)
    # setupUi

    def retranslateUi(self, AccessMapScreen):
        AccessMapScreen.setWindowTitle(QCoreApplication.translate("AccessMapScreen", u"Form", None))
        self.checkBox_3.setText(QCoreApplication.translate("AccessMapScreen", u"Obstacles", None))
        self.checkBox.setText(QCoreApplication.translate("AccessMapScreen", u"Toilets", None))
        self.checkBox_2.setText(QCoreApplication.translate("AccessMapScreen", u"Parking", None))
    # retranslateUi

