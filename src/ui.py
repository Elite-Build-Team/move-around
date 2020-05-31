# -*- coding: utf-8 -*-
import os
import sys
from typing import List

from PySide2 import QtCore, QtWidgets, QtQuickWidgets, QtPositioning
from PySide2 import QtGui
from PySide2.QtCore import QUrl
from PySide2.QtQuickWidgets import QQuickWidget
from PySide2.QtWidgets import QFileDialog
from PySide2 import QtCore, QtWidgets, QtGui

from dummy_model import *


class AccessMapScreen(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.toilets_checkbox = QtWidgets.QCheckBox("Toilets")
        self.parkings_checkbox = QtWidgets.QCheckBox("Parkings")
        self.obstacles_checkbox = QtWidgets.QCheckBox("Obstacles")
        self.button_back = QtWidgets.QPushButton("Done")

        self.toilets_checkbox.stateChanged.connect(self.show_toilets)
        self.parkings_checkbox.stateChanged.connect(self.show_parkings)
        self.obstacles_checkbox.stateChanged.connect(self.show_obstacles)
        self.button_back.clicked.connect(self.on_done_clicked)

        self.layout = QtWidgets.QVBoxLayout()

        self.map = MapWidget()
        self.layout.addWidget(self.map)

        self.checkbox_layout = QtWidgets.QHBoxLayout()
        self.checkbox_layout.addWidget(self.toilets_checkbox)
        self.checkbox_layout.addWidget(self.parkings_checkbox)
        self.checkbox_layout.addWidget(self.obstacles_checkbox)
        self.checkbox_layout.addWidget(self.button_back)

        self.layout.addLayout(self.checkbox_layout)

        self.setLayout(self.layout)
        self.resize(720, 480)

    def on_done_clicked(self):
        self.show_popup()

    def show_toilets(self):
        if self.toilets_checkbox.isChecked():
            self.map.show_location_type(LocationType.Toilet)
        else:
            self.map.hide_location_type(LocationType.Toilet)

    def show_parkings(self):
        if self.parkings_checkbox.isChecked():
            self.map.show_location_type(LocationType.Parking)
        else:
            self.map.hide_location_type(LocationType.Parking)

    def show_obstacles(self):
        if self.obstacles_checkbox.isChecked():
            self.map.show_location_type(LocationType.Obstacle)
        else:
            self.map.hide_location_type(LocationType.Obstacle)

    def show_popup(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Αναφορά Προβλήματος")
        msg.setText("Θα θέλατε να κάνετε κάποια αναφορά;")
        msg.setIcon(QtWidgets.QMessageBox.Question)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        msg.setDefaultButton(QtWidgets.QMessageBox.Ok)
        
        msg.buttonClicked.connect(self.button_do)
        msg.exec_()

    def button_do(self, i):
        if i.text() == '&OK':
            app.show_screen(ChooseLocationScreen())
        else:
            app.show_screen(MainScreen())
            

class MarkerModel(QtCore.QAbstractListModel):
    PositionRole, SourceRole = range(QtCore.Qt.UserRole, QtCore.Qt.UserRole + 2)

    def __init__(self, parent=None):
        super(MarkerModel, self).__init__(parent)
        self._markers = []

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self._markers)

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if 0 <= index.row() < self.rowCount():
            if role == MarkerModel.PositionRole:
                return self._markers[index.row()]["position"]
            elif role == MarkerModel.SourceRole:
                return self._markers[index.row()]["source"]
        return QtCore.QVariant()

    def roleNames(self):
        return {MarkerModel.PositionRole: b"position_marker", MarkerModel.SourceRole: b"source_marker"}

    def appendMarker(self, marker):
        self.beginInsertRows(QtCore.QModelIndex(), self.rowCount(), self.rowCount())
        self._markers.append(marker)
        self.endInsertRows()

    def removeMarker(self, marker):
        # self.beginRemoveRows(QtCore.QModelIndex(), self.rowCount(), self.rowCount())
        # self._markers.remove(marker)
        # self.endRemoveRows()
        # TODO
        raise NotImplementedError()


class MapWidget(QtQuickWidgets.QQuickWidget):
    def __init__(self, parent=None):
        super(MapWidget, self).__init__(parent,
                                        resizeMode=QtQuickWidgets.QQuickWidget.SizeRootObjectToView)
        self.marker_model = MarkerModel(self)
        self.access_map = model.access_map
        self.rootContext().setContextProperty("markermodel", self.marker_model)
        qml_path = os.path.join(os.path.dirname(__file__), "qml/access-map.qml")
        self.setSource(QtCore.QUrl.fromLocalFile(qml_path))
        self.urls = {LocationType.Parking:"../resources/parking.png",
                     LocationType.Obstacle:"../resources/obstacle.png", LocationType.Toilet:"../resources/toilet.png"}

    def show_location_type(self, location_type: LocationType):
        for location in self.access_map.get_locations_by_type(location_type):
            coord = QtPositioning.QGeoCoordinate(*location.get_coordinates())
            source = QtCore.QUrl(self.urls[location_type])
            # TODO Change icons
            self.marker_model.appendMarker({"position": coord, "source": source})

    def hide_location_type(self, location_type: LocationType):
        # for location in self.access_map.get_locations_by_type(location_type):
        #     self.marker_model.removeMarker("position": coord, "source": source})
        # TODO
        raise NotImplementedError()


class ChoosePhotographScreen(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.button_input_file = QtWidgets.QToolButton()
        self.text_edit_photograph = QtWidgets.QLineEdit()
        self.button_submit_report = QtWidgets.QPushButton("Choose Photograph")
        self.preview_photograph = QtWidgets.QLabel()

        self.button_input_file.clicked.connect(self.on_input_file_clicked)
        self.button_submit_report.clicked.connect(self.on_choose_photograph_clicked)

        self.layout1 = QtWidgets.QHBoxLayout()
        self.layout1.addWidget(self.button_input_file)
        self.layout1.addWidget(self.text_edit_photograph)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addLayout(self.layout1)
        self.layout.addWidget(self.button_submit_report)
        self.layout.addWidget(self.preview_photograph)
        self.setLayout(self.layout)
        self.resize(720, 480)

    def on_input_file_clicked(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Open file', dir='.')
        types ={".png", '.jpg'}
        if filename:
            if not self.photograph[-4:] in types:
                self.show_invalid_photo_type()
                app.show_screen(ChoosePhotographScreen())
            else: 
                self.text_edit_photograph.setText(filename)
                self.photograph = QtGui.QPixmap(filename)
                self.photograph = self.photograph.scaled(700, 700, QtCore.Qt.KeepAspectRatio)
                self.preview_photograph.setPixmap(self.photograph)
                self.preview_photograph.setScaledContents(True)

    def on_choose_photograph_clicked(self):
        #TODO
        #model.report_issue.set_photograph(self.photograph)
        
        issue_description_screen = IssueDescriptionScreen()
        app.show_screen(issue_description_screen)

    def show_invalid_photo_type(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Εσφαλμένο είδος αρχείου")
        msg.setText("Δόθηκε λάθος τύπος σαν είσοδος. Aποδεκτοί τύποι αρχείων .jpg και .png")
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.exec_()

class ChooseLocationScreen(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.button_choose_location = QtWidgets.QPushButton("Choose Location")
        self.button_choose_location.clicked.connect(self.on_choose_location_clicked)
        self.layout = QtWidgets.QVBoxLayout()

        # self.horizontal_layout = QtWidgets.QHBoxLayout()
        self.pin_location = PinLocation()
        qml_path = os.path.join(os.path.dirname(__file__), "qml/choose-location.qml")
        self.quickWidget = QQuickWidget(QUrl.fromLocalFile(qml_path))
        self.quickWidget.rootContext().setContextProperty("pin_location", self.pin_location)
        self.quickWidget.setResizeMode(QtQuickWidgets.QQuickWidget.SizeRootObjectToView)
        self.layout.addWidget(self.quickWidget)
        self.layout.addWidget(self.button_choose_location)
        self.setLayout(self.layout)
        self.resize(720, 480)

    def on_choose_location_clicked(self):
        #TODO
        model.report_issue = ReportIssue()
        if not self.pin_location.lat or not self.pin_location.lon:
            self.show_popup()
            app.show_screen(ChooseLocationScreen())
        else:
            model.report_issue.set_location(Location((self.pin_location.lat, self.pin_location.lon), LocationType.Obstacle))
            app.show_screen(ChoosePhotographScreen())

#TODO Find a better name
class PinLocation(QtCore.QObject):
    def __init__(self, parent=None):
        QtCore.QObject.__init__(self, parent)
        self._lon: float = 0
        self._lat: float = 0

    @QtCore.Property(float)
    def lon(self):
        return self._lon

    @lon.setter
    def setLon(self, lon):
        if self._lon == lon:
            return
        self._lon = lon
    
    @QtCore.Property(float)
    def lat(self):
        return self._lat

    @lat.setter
    def setLat(self, lat):
        if self._lat == lat:
            return
        self._lat = lat


class IssueDescriptionScreen(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.text_edit_description = QtWidgets.QTextEdit()
        self.button_submit_report = QtWidgets.QPushButton("Submit Report")
        self.button_submit_report.clicked.connect(self.on_submit_clicked)
        

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.text_edit_description)
        self.layout.addWidget(self.button_submit_report)
        self.setLayout(self.layout)
        self.resize(720, 480)

    def on_submit_clicked(self):
        ms = MainScreen()
        app.show_screen(ms)
        if not self.text_edit_description.toPlainText():
            self.show_popup()
            app.show_screen(IssueDescriptionScreen())
        else:
            model.report_issue.set_summary(self.text_edit_description.toPlainText())
            model.pending_issues.add_pending_issue(model.report_issue)
            model.access_map.add_location(model.report_issue.get_location())
            model.amea.add_report_issue(model.report_issue)

    def show_popup(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Αδυναμία Αποστολής Αναφοράς")
        msg.setText("Δεν έχει εισαχθεί περιγραφή. Παρακαλώ συμπληρώστε ξανά.")
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.exec_()

  

class MainScreen(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.welcome_message = QtWidgets.QLabel("Welcome to Move-around!")
        self.button_report_issue = QtWidgets.QPushButton("Report Issue")
        self.button_access_map = QtWidgets.QPushButton("Access Map")

        self.button_report_issue.clicked.connect(self.on_report_issue_clicked)
        self.button_access_map.clicked.connect(self.on_access_map_clicked)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.welcome_message)
        self.layout.addWidget(self.button_report_issue)
        self.layout.addWidget(self.button_access_map)
        self.setLayout(self.layout)
        self.resize(720, 480)

    def on_report_issue_clicked(self):
        choose_location_screen = ChooseLocationScreen()
        app.show_screen(choose_location_screen)

    def on_access_map_clicked(self):
        access_map_screen = AccessMapScreen()
        app.show_screen(access_map_screen)


class Application(QtWidgets.QWidget):
    def __init__(self, ):
        super().__init__()
        self.layout = QtWidgets.QVBoxLayout()
        self.widget = None
        self.setLayout(self.layout)
        self.resize(720, 480)

    def show_screen(self, widget):
        if self.widget is not None:
            self.layout.removeWidget(self.widget)
            self.widget.close()

        self.widget = widget
        self.layout.addWidget(self.widget)
        self.layout.update()


if __name__ == '__main__':
    model: 'DummyModel' = DummyModel()

    qapp = QtWidgets.QApplication([])
    qapp.setApplicationName('Move Around')
    app = Application()
    app.resize(720, 480)
    app.show()

    main_screen = MainScreen()
    app.show_screen(main_screen)

    sys.exit(qapp.exec_())
