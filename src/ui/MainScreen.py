# -*- coding: utf-8 -*-

import sys
import random
from PySide2 import QtWidgets

from PySide2 import QtCore, QtWidgets, QtGui

class MainScreenWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.welcome_message = QtWidgets.QLabel("Welcome to Move-around!")
        self.button_report_issue = QtWidgets.QPushButton("Report Issue")
        self.button_access_map = QtWidgets.QPushButton("Access Map")

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.welcome_message)
        self.layout.addWidget(self.button_report_issue)
        self.layout.addWidget(self.button_access_map)
        self.setLayout(self.layout)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MainScreenWidget()
    widget.resize(400, 300)
    widget.show()

    sys.exit(app.exec_())