import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    visible: true
    width: 350
    height: 300
    title: "Python-QML Counter Link"

    Rectangle {
        anchors.fill: parent
        color: "#2b84dd"

        ColumnLayout {
            anchors.centerIn: parent
            spacing: 25

            Text {
                Layout.alignment: Qt.AlignHCenter
                // Automatically updates because it reads from the Python property
                text: "Python Count: " + counterBackend.currentCount
                font.pixelSize: 26
                font.bold: true
                color: "#212529"
            }

            Button {
                Layout.alignment: Qt.AlignHCenter
                text: "Click to Increment Backend"
                font.pointSize: 12                
                // Changes the button background to solid dark blue
                palette.button: "#00000000" 
                // Forces the text to be crisp white for high contrast
                palette.buttonText: "#ffffff" 
                
                onClicked: {
                    counterBackend.increment = true
                }
            }
        }
    }
}
