# -*- coding: utf-8 -*-

import sys
import random
from PySide2 import QtWidgets

from PySide2 import QtCore, QtWidgets, QtGui

from PySide2.QtWidgets import QApplication
from PySide2.QtQuickWidgets import QQuickWidget
from PySide2.QtCore import QUrl


class PhotographSelectionScreen(QtWidgets.QWidget):
    def setupUi(self, ReportIssueScreen2):
        if not ReportIssueScreen2.objectName():
            ReportIssueScreen2.setObjectName(u"ReportIssueScreen2")
        ReportIssueScreen2.resize(398, 298)
        self.verticalLayout = QtWidgets.QVBoxLayout(ReportIssueScreen2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
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
        self.pushButton.setText(QCoreApplication.translate("ReportIssueScreen2", u"Choose Photograph", None))
    # retranslateUi

