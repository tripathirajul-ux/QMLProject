from PyQt6.QtCore import QObject, pyqtProperty, pyqtSignal, QTimer

class ProgressBackend(QObject):
    progress_changed = pyqtSignal(float)
    interval_changed = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self._progress = 0.0
        self._interval = 50  
        self._moving_forward = True

        # Core logic loop driven by Python
        self.timer = QTimer()
        self.timer.setInterval(self._interval)
        self.timer.timeout.connect(self._update_progress)
        self.timer.start()

    def _update_progress(self):
        if self._moving_forward:
            self._progress += 0.01
            if self._progress >= 1.0:
                self._progress = 1.0
                self._moving_forward = False
        else:
            self._progress -= 0.01
            if self._progress <= 0.0:
                self._progress = 0.0
                self._moving_forward = True
        
        self.progress_changed.emit(self._progress)

    @pyqtProperty(float, notify=progress_changed)
    def progress(self):
        return self._progress

    @pyqtProperty(int, notify=interval_changed)
    def interval(self):
        return self._interval

    @interval.setter
    def interval(self, value):
        if value > 0 and self._interval != value:
            self._interval = value
            self.timer.setInterval(self._interval)
            self.interval_changed.emit(self._interval)

    @pyqtProperty(float)
    def start_point(self):
        return self._progress

    @start_point.setter
    def start_point(self, value):
        if 0.0 <= value <= 1.0:
            self._progress = value
            self.progress_changed.emit(self._progress)
