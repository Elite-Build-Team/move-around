# -*- coding: utf-8 -*-

import sys
import random
from PySide2 import QtWidgets

from PySide2 import QtCore, QtWidgets, QtGui

from PySide2.QtWidgets import QApplication
from PySide2.QtQuickWidgets import QQuickWidget
from PySide2.QtCore import QUrl

class ReportIssueScreen1Widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.button_choose_location = QtWidgets.QPushButton("Choose Location")

        self.layout = QtWidgets.QVBoxLayout()

        # self.horizontal_layout = QtWidgets.QHBoxLayout()

        self.quickWidget = QQuickWidget(QUrl('src/ui/choose-location.qml'))
        self.layout.addWidget(self.quickWidget)
        self.layout.addWidget(self.button_choose_location)
        self.setLayout(self.layout)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = ReportIssueScreen1Widget()
    widget.resize(400, 300)
    widget.show()

    sys.exit(app.exec_())