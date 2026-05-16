import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    visible: true
    width: 550
    height: 650
    title: "9x9 Reflex Grid Challenge"

    Rectangle {
        anchors.fill: parent
        color: "#1e1e24"

        ColumnLayout {
            anchors.fill: parent
            anchors.margins: 20
            spacing: 15

            // Dashboard Header Controls
            RowLayout {
                Layout.fillWidth: true
                spacing: 20

                Button {
                    text: "START GAME"
                    font.bold: true
                    onClicked: gameBackend.start_game = true
                }

                Text {
                    text: "Universal Clock: " + gameBackend.universalTimeStr
                    color: "#ffffff"
                    font.pixelSize: 18
                    font.bold: true
                    Layout.fillWidth: true
                    horizontalAlignment: Text.AlignRight
                }
                Column {
    spacing: 5

                Text {
                    text: "TOP SCORES"
                    color: "yellow"
                    font.bold: true
                    font.pixelSize: 18
                }

                Repeater {
                    model: gameBackend.topScores

                    delegate: Text {
                        text: (index + 1) + ". " + modelData
                        color: "white"
                        font.pixelSize: 16
                    }
                }
            }
            }

            // Master 9x9 Play Area Container
            Item {
                Layout.fillWidth: true
                Layout.fillHeight: true

                Grid {
                    id: chessGrid
                    anchors.centerIn: parent
                    rows: 9
                    columns: 9
                    spacing: 2

                    // Calculate bounding limits box size to maintain grid shape symmetry
                    property real squareSize: Math.min((parent.width - 16) / 9, (parent.height - 16) / 9)

                    Repeater {
                        model: 81 // 9 rows * 9 columns = 81 total block fields
                        delegate: Rectangle {
                            width: chessGrid.squareSize
                            height: chessGrid.squareSize

                            // Calculate checkered grid values based on row/column positioning
                            property int rowIdx: Math.floor(index / 9)
                            property int colIdx: index % 9
                            property bool isDark: (rowIdx + colIdx) % 2 === 1

                            // State checking logic: turn cell red if index matches target selection
                            color: gameBackend.redIndex === index ? "#ff3333" : (isDark ? "#2b2d42" : "#8d99ae")
                            border.color: "#111115"
                            border.width: 1

                            // Turns the tile into a circle only when it becomes the red target bomb
                            radius: gameBackend.redIndex === index ? (width / 2) : 4 


                            MouseArea {
                                anchors.fill: parent
                                onClicked: {
                                    // Ship targeted index position off to python state verification engine
                                    gameBackend.handle_click = index
                                }
                            }
                        }
                    }
                }

                // Modal Overlaid Alert Panel popped visible upon runtime system exceptions
                Rectangle {
                    anchors.fill: chessGrid
                    color: "#f2000000" // Semi transparent black veil
                    visible: gameBackend.isGameOver
                    radius: 13

                    ColumnLayout {
                        anchors.centerIn: parent
                        spacing: 15

                        Text {
                            text: "GAME OVER"
                            color: "#ff3333"
                            font.pixelSize: 28
                            font.bold: true
                            Layout.alignment: Qt.AlignHCenter
                        }

                        Text {
                            text: "Total Time Survived:"
                            color: "#ffffff"
                            font.pixelSize: 14
                            Layout.alignment: Qt.AlignHCenter
                        }

                        Text {
                            text: gameBackend.finalTimeStr
                            color: "#00ffcc"
                            font.pixelSize: 22
                            font.bold: true
                            Layout.alignment: Qt.AlignHCenter
                        }
                        
                        Text {
                            text: "Click START GAME to try again"
                            color: "#aaaaaa"
                            font.pixelSize: 12
                            Layout.alignment: Qt.AlignHCenter
                        }
                    }
                }
            }
        }
    }
}
