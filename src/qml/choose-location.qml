import QtQuick 2.0
import QtLocation 5.6
import QtPositioning 5.6

Item {
    width: 720
    height: 480

    Plugin {
        id: osmPlugin
        name: "osm"
    }

    Map {
        id: map
        anchors.fill: parent
        plugin: osmPlugin
        center: QtPositioning.coordinate(38.246473, 21.734790)
        zoomLevel: 20
    }

    MouseArea {
        acceptedButtons: Qt.RightButton
        anchors.fill: parent
        onClicked:  {
            var selected_location = map.toCoordinate(Qt.point(mouse.x,mouse.y))
            pin_location.lon = selected_location.longitude
            pin_location.lat = selected_location.latitude
        }
    }
}