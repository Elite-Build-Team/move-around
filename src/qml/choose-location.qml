import QtQuick 2.0
import QtLocation 5.6
import QtPositioning 5.6

Item {
    width: 400
    height: 300

    Plugin {
        id: mapPlugin
        name: "osm"
    }

    Map {
        anchors.fill: parent
        plugin: mapPlugin
        center: QtPositioning.coordinate(38.24, 21.73)
        zoomLevel: 16
    }

    MouseArea {
        anchors.fill: parent
        onPressed: {
            marker.coordinate = map.toCoordinate(Qt.point(mouse.x,mouse.y))
        }
    }
}