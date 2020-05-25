# -*- coding: utf-8 -*-

import sys

from PySide2 import QtCore, QtWidgets


class MainScreenWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.welcome_message = QtWidgets.QLabel("Welcome to Move-around!")
        self.button_report_issue = QtWidgets.QPushButton("Report Issue")
        self.button_access_map = QtWidgets.QPushButton("Access Map")

        self.button_report_issue.clicked.connect(self.report_issue_clicked)
        self.button_access_map.clicked.connect(self.access_map_clicked)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.welcome_message)
        self.layout.addWidget(self.button_report_issue)
        self.layout.addWidget(self.button_access_map)
        self.setLayout(self.layout)
        self.resize(400, 300)

    @QtCore.Slot
    def report_issue_clicked(self):
        pass

    @QtCore.Slot
    def access_map_clicked(self):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MainScreenWidget()
    widget.resize(400, 300)
    widget.show()

    sys.exit(app.exec_())
