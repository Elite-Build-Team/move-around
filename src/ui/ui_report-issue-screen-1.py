# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'report-issue-screen-1NhJCvb.ui'
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



class Ui_ReportIssueScreen1(object):
    def setupUi(self, ReportIssueScreen1):
        if not ReportIssueScreen1.objectName():
            ReportIssueScreen1.setObjectName(u"ReportIssueScreen1")
        ReportIssueScreen1.resize(400, 300)
        self.verticalLayout_2 = QVBoxLayout(ReportIssueScreen1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(ReportIssueScreen1)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.quickWidget = QQuickWidget(self.widget)
        self.quickWidget.setObjectName(u"quickWidget")
        self.quickWidget.setResizeMode(QQuickWidget.SizeRootObjectToView)

        self.verticalLayout_3.addWidget(self.quickWidget)


        self.verticalLayout.addWidget(self.widget)

        self.pushButton = QPushButton(ReportIssueScreen1)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(ReportIssueScreen1)

        QMetaObject.connectSlotsByName(ReportIssueScreen1)
    # setupUi

    def retranslateUi(self, ReportIssueScreen1):
        ReportIssueScreen1.setWindowTitle(QCoreApplication.translate("ReportIssueScreen1", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("ReportIssueScreen1", u"Choose Location", None))
    # retranslateUi

