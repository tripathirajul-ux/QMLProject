import sys
import os

# 1. Force the engine to use the fallback "Basic" style to avoid Windows DLL errors
os.environ["QT_QUICK_CONTROLS_STYLE"] = "Basic"

# 2. Dynamic environment path mapping
base_dir = os.path.dirname(os.path.abspath(__file__))

# 3. Look up one level to find the .venv folder structure automatically
project_root = os.path.dirname(base_dir)
venv_site_packages = os.path.join(project_root, ".venv", "Lib", "site-packages")
qt_bin_dir = os.path.join(venv_site_packages, "PyQt6", "Qt6", "bin")

# 4. Inject strict binary loading paths for Windows kernel safety
if os.path.exists(qt_bin_dir):
    os.environ["PATH"] = qt_bin_dir + os.pathsep + os.environ["PATH"]
    if hasattr(os, "add_dll_directory"):
        os.add_dll_directory(qt_bin_dir)

os.environ["QT_PLUGIN_PATH"] = os.path.join(venv_site_packages, "PyQt6", "Qt6", "plugins")
os.environ["QML2_IMPORT_PATH"] = os.path.join(venv_site_packages, "PyQt6", "Qt6", "qml")

# 5. Initialize Framework after setting environmental safety boundaries
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine
from backend import ProgressBackend

app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()

# Connect backend class to QML context
backend_controller = ProgressBackend()
engine.rootContext().setContextProperty("progressBackend", backend_controller)

# Load layout
qml_path = os.path.join(base_dir, 'main.qml')
engine.load(qml_path)

if not engine.rootObjects():
    sys.exit(-1)

sys.exit(app.exec())
