import sys
import os

# Enforce Basic rendering style to bypass OneDrive style environment errors
os.environ["QT_QUICK_CONTROLS_STYLE"] = "Basic"

base_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(base_dir)
venv_site_packages = os.path.join(project_root, ".venv", "Lib", "site-packages")
qt_bin_dir = os.path.join(venv_site_packages, "PyQt6", "Qt6", "bin")

if os.path.exists(qt_bin_dir):
    os.environ["PATH"] = qt_bin_dir + os.pathsep + os.environ["PATH"]
    if hasattr(os, "add_dll_directory"):
        os.add_dll_directory(qt_bin_dir)

os.environ["QT_PLUGIN_PATH"] = os.path.join(venv_site_packages, "PyQt6", "Qt6", "plugins")
os.environ["QML2_IMPORT_PATH"] = os.path.join(venv_site_packages, "PyQt6", "Qt6", "qml")

from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine
from backend import GameBackend

app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()

game_controller = GameBackend()
engine.rootContext().setContextProperty("gameBackend", game_controller)

qml_path = os.path.join(base_dir, 'main.qml')
engine.load(qml_path)

if not engine.rootObjects():
    sys.exit(-1)

sys.exit(app.exec())
