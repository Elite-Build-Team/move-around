# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'report-issue-screen-2gulruH.ui'
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

from kimagefilepreview import KImageFilePreview


class Ui_ReportIssueScreen2(object):
    def setupUi(self, ReportIssueScreen2):
        if not ReportIssueScreen2.objectName():
            ReportIssueScreen2.setObjectName(u"ReportIssueScreen2")
        ReportIssueScreen2.resize(400, 300)
        self.verticalLayout = QVBoxLayout(ReportIssueScreen2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.kimagefilepreview = KImageFilePreview(ReportIssueScreen2)
        self.kimagefilepreview.setObjectName(u"kimagefilepreview")

        self.gridLayout.addWidget(self.kimagefilepreview, 0, 0, 1, 1)

        self.pushButton = QPushButton(ReportIssueScreen2)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(ReportIssueScreen2)

        QMetaObject.connectSlotsByName(ReportIssueScreen2)
    # setupUi

    def retranslateUi(self, ReportIssueScreen2):
        ReportIssueScreen2.setWindowTitle(QCoreApplication.translate("ReportIssueScreen2", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("ReportIssueScreen2", u"\u0395\u03c0\u03b9\u03bb\u03bf\u03b3\u03ae \u03a6\u03c9\u03c4\u03bf\u03b3\u03c1\u03b1\u03c6\u03af\u03b1\u03c2", None))
    # retranslateUi

