import sys
import os
import subprocess

from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtCore import QObject, pyqtSlot


class LauncherBackend(QObject):

    @pyqtSlot(str)
    def openApp(self, app_name):

        # Folder containing THIS main.py
        current_dir = os.path.dirname(__file__)

        # Go one level up → NEW_PROJECT
        project_root = os.path.dirname(current_dir)

        if app_name == "Simple Counter":

            app_path = os.path.join(
                project_root,
                "Project1",
                "main.py"
            )

            subprocess.Popen(
                [sys.executable, app_path]
            )

        elif app_name == "Progress Bar":

            app_path = os.path.join(
                project_root,
                "Project2",
                "main.py"
            )

            subprocess.Popen(
                [sys.executable, app_path]
            )

        elif app_name == "Bomb Game":

            app_path = os.path.join(
                project_root,
                "Project3",
                "main.py"
            )

            subprocess.Popen(
                [sys.executable, app_path]
            )


app = QGuiApplication(sys.argv)

engine = QQmlApplicationEngine()

backend = LauncherBackend()

engine.rootContext().setContextProperty(
    "launcherBackend",
    backend
)

qml_path = os.path.join(
    os.path.dirname(__file__),
    "main.qml"
)

engine.load(qml_path)

if not engine.rootObjects():
    sys.exit(-1)

sys.exit(app.exec())