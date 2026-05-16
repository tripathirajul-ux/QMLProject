import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    visible: true
    width: 450
    height: 400
    title: "Isolated Progress Bar Project"

    Rectangle {
        anchors.fill: parent
        color: "#f0f2f5"

        ColumnLayout {
            anchors.fill: parent
            anchors.margins: 25
            spacing: 20

            Text {
                Layout.alignment: Qt.AlignHCenter
                text: "Python Engine Progress Controller"
                font.pixelSize: 18
                font.bold: true
            }

            // Binds value to Python: progressBackend.progress
            ProgressBar {
                id: controlBar
                Layout.fillWidth: true
                value: progressBackend.progress 
            }

            // Group 1: Frequency / Speed Control
            RowLayout {
                Layout.fillWidth: true
                spacing: 10

                TextField {
                    id: speedInput
                    placeholderText: "Interval (ms)"
                    text: progressBackend.interval.toString()
                    inputMethodHints: Qt.ImhDigitsOnly
                    Layout.fillWidth: true
                }

                Button {
                    text: "Set Frequency"
                    onClicked: {
                        let val = parseInt(speedInput.text)
                        if (!isNaN(val)) {
                            progressBackend.interval = val
                        }
                    }
                }
            }

            // Group 2: Jump-to-Start Point Control
            RowLayout {
                Layout.fillWidth: true
                spacing: 10

                TextField {
                    id: startInput
                    placeholderText: "Jump value (0.0 to 1.0)"
                    text: "0.0"
                    Layout.fillWidth: true
                }

                Button {
                    text: "Set Start Point"
                    onClicked: {
                        let val = parseFloat(startInput.text)
                        if (!isNaN(val)) {
                            progressBackend.start_point = val
                        }
                    }
                }
            }
            
            Item { Layout.fillHeight: true }
        }
    }
}
