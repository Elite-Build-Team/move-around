# -*- coding: utf-8 -*-

import sys
import random
from PySide2 import QtWidgets

from PySide2 import QtCore, QtWidgets, QtGui


class ReportIssueScreen3Widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.text_edit_description = QtWidgets.QTextEdit()
        self.button_submit_report = QtWidgets.QPushButton("Submit Report")

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.text_edit_description)
        self.layout.addWidget(self.button_submit_report)
        self.setLayout(self.layout)
        self.resize(400, 300)
