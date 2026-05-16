import QtQuick
import QtQuick.Controls
import QtQuick.Window

ApplicationWindow {

    visible: true
    width: 900
    height: 700
    title: "Mini Game Launcher"

    color: "#1e1e1e"

    Rectangle {
        anchors.fill: parent
        color: "#1e1e1e"

        // COUNTER BOX
        Rectangle {

            id: counterBox

            width: 170
            height: 100

            radius: 15
            color: "#3498db"

            x: 50
            y: 80

            Text {
                anchors.centerIn: parent
                text: "COUNTER"
                color: "white"
                font.pixelSize: 22
                font.bold: true
            }

            MouseArea {
                anchors.fill: parent

                onClicked: {
                    launcherBackend.openApp("Simple Counter")
                }
            }

            SequentialAnimation on x {
                loops: Animation.Infinite

                NumberAnimation {
                    to: 650
                    duration: 3000
                }

                NumberAnimation {
                    to: 50
                    duration: 3000
                }
            }

            SequentialAnimation on y {
                loops: Animation.Infinite

                NumberAnimation {
                    to: 500
                    duration: 2500
                }

                NumberAnimation {
                    to: 80
                    duration: 2500
                }
            }
        }

        // PROGRESS BAR BOX
        Rectangle {

            id: progressBox

            width: 170
            height: 100

            radius: 15
            color: "#2ecc71"

            x: 400
            y: 200

            Text {
                anchors.centerIn: parent
                text: "PROGRESS BAR"
                color: "white"
                font.pixelSize: 20
                font.bold: true
            }

            MouseArea {
                anchors.fill: parent

                onClicked: {
                    launcherBackend.openApp("Progress Bar")
                }
            }

            SequentialAnimation on x {
                loops: Animation.Infinite

                NumberAnimation {
                    to: 100
                    duration: 4000
                }

                NumberAnimation {
                    to: 600
                    duration: 4000
                }
            }

            SequentialAnimation on y {
                loops: Animation.Infinite

                NumberAnimation {
                    to: 450
                    duration: 3500
                }

                NumberAnimation {
                    to: 150
                    duration: 3500
                }
            }
        }

        // BOMB GAME BOX
        Rectangle {

            id: bombBox

            width: 170
            height: 100

            radius: 15
            color: "#e74c3c"

            x: 250
            y: 450

            Text {
                anchors.centerIn: parent
                text: "BOMB GAME"
                color: "white"
                font.pixelSize: 20
                font.bold: true
            }

            MouseArea {
                anchors.fill: parent

                onClicked: {
                    launcherBackend.openApp("Bomb Game")
                }
            }

            SequentialAnimation on x {
                loops: Animation.Infinite

                NumberAnimation {
                    to: 700
                    duration: 5000
                }

                NumberAnimation {
                    to: 100
                    duration: 5000
                }
            }

            SequentialAnimation on y {
                loops: Animation.Infinite

                NumberAnimation {
                    to: 100
                    duration: 3000
                }

                NumberAnimation {
                    to: 500
                    duration: 3000
                }
            }
        }
    }
}