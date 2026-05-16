import sys
import os
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtCore import QObject, pyqtProperty, pyqtSignal

class CounterBackend(QObject):
    counter_changed = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self._count = 0

    @pyqtProperty(int, notify=counter_changed)
    def currentCount(self):
        return self._count

    @pyqtProperty(bool)
    def increment(self):
        return True

    @increment.setter 
    def increment(self, value):
        if value:
            self._count += 1
            self.counter_changed.emit(self._count)

app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()

backend = CounterBackend()
engine.rootContext().setContextProperty("counterBackend", backend)

# Loads main.qml from the exact folder where this file runs
engine.load(os.path.join(os.path.dirname(__file__), 'main.qml'))

if not engine.rootObjects():
    sys.exit(-1)

sys.exit(app.exec())
