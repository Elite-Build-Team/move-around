# -*- coding: utf-8 -*-

import sys
import random
from PySide2 import QtWidgets

from PySide2 import QtCore, QtWidgets, QtGui

from PySide2.QtWidgets import QApplication
from PySide2.QtQuickWidgets import QQuickWidget
from PySide2.QtCore import QUrl

class AccessMapWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.toilets_checkbox = QtWidgets.QCheckBox("Toilets")
        self.parkings_checkbox = QtWidgets.QCheckBox("Parkings")
        self.obstacles_checkbox = QtWidgets.QCheckBox("Obstacles")

        self.layout = QtWidgets.QVBoxLayout()

        # self.horizontal_layout = QtWidgets.QHBoxLayout()
        self.quickWidget = QQuickWidget(QUrl('src/ui/access-map.qml'))
        self.layout.addWidget(self.quickWidget)
        
        self.checkbox_layout = QtWidgets.QHBoxLayout()
        self.checkbox_layout.addWidget(self.toilets_checkbox)
        self.checkbox_layout.addWidget(self.parkings_checkbox)
        self.checkbox_layout.addWidget(self.obstacles_checkbox)

        self.layout.addLayout(self.checkbox_layout)
        
        self.setLayout(self.layout)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = AccessMapWidget()
    widget.resize(400, 300)
    widget.show()

    sys.exit(app.exec_())