# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'report-issue-screen-3wupLyD.ui'
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


class Ui_ReportIssueScreen3(object):
    def setupUi(self, ReportIssueScreen3):
        if not ReportIssueScreen3.objectName():
            ReportIssueScreen3.setObjectName(u"ReportIssueScreen3")
        ReportIssueScreen3.resize(400, 300)
        self.verticalLayout_2 = QVBoxLayout(ReportIssueScreen3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.plainTextEdit = QPlainTextEdit(ReportIssueScreen3)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.verticalLayout.addWidget(self.plainTextEdit)

        self.pushButton = QPushButton(ReportIssueScreen3)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(ReportIssueScreen3)

        QMetaObject.connectSlotsByName(ReportIssueScreen3)
    # setupUi

    def retranslateUi(self, ReportIssueScreen3):
        ReportIssueScreen3.setWindowTitle(QCoreApplication.translate("ReportIssueScreen3", u"Form", None))
#if QT_CONFIG(tooltip)
        self.plainTextEdit.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setPlaceholderText(QCoreApplication.translate("ReportIssueScreen3", u"\u0395\u03b9\u03c3\u03ac\u03b3\u03b5\u03c4\u03b5 \u03c0\u03b5\u03c1\u03b9\u03b3\u03c1\u03b1\u03c6\u03ae \u03c4\u03b7\u03c2 \u03b2\u03bb\u03ac\u03b2\u03b7\u03c2.", None))
        self.pushButton.setText(QCoreApplication.translate("ReportIssueScreen3", u"\u03a5\u03c0\u03bf\u03b2\u03bf\u03bb\u03ae \u0392\u03bb\u03ac\u03b2\u03b7\u03c2", None))
    # retranslateUi

