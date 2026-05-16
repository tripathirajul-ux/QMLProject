import random
import time
from PyQt6.QtCore import QObject, pyqtProperty, pyqtSignal, QTimer
import heapq

max_heap = []

class GameBackend(QObject):
    # Signals to alert the QML layout of data updates
    red_index_changed = pyqtSignal(int)
    game_over_changed = pyqtSignal(bool)
    final_time_changed = pyqtSignal(str)
    universal_time_changed = pyqtSignal(str)
    top_scores_changed = pyqtSignal()

    def __init__(self):
        super().__init__()
        self._red_index = -1
        self._is_game_over = False
        self._final_time_str = "0.0s"
        self._universal_time_str = "0.0s"

        # Game Tracking Variables
        self.start_time = 0.0
        self.base_reaction_limit = 2000  # Starts with 2 seconds (2000ms)
        self.current_reaction_limit = 2000
        self.minimum_reaction_limit = 400 # Will not go faster than 400ms

        # Timers
        self.universal_timer = QTimer()
        self.universal_timer.setInterval(100) # Updates display every 100ms
        self.universal_timer.timeout.connect(self._update_universal_clock)

        self.reaction_timer = QTimer()
        self.reaction_timer.setSingleShot(True)
        self.reaction_timer.timeout.connect(self._handle_time_up)

    @pyqtProperty(int, notify=red_index_changed)
    def redIndex(self):
        return self._red_index

    @pyqtProperty(bool, notify=game_over_changed)
    def isGameOver(self):
        return self._is_game_over

    @pyqtProperty(str, notify=final_time_changed)
    def finalTimeStr(self):
        return self._final_time_str

    @pyqtProperty(str, notify=universal_time_changed)
    def universalTimeStr(self):
        return self._universal_time_str

    # Invokable method triggered by the frontend Start Button
    @pyqtProperty(bool)
    def start_game(self):
        return True
    
    @pyqtProperty('QStringList', notify=top_scores_changed)
    def topScores(self):
        return [f"{score:.2f}s" for score in sorted(max_heap, reverse=True)]

    @start_game.setter
    def start_game(self, value):
        if value:
            self._is_game_over = False
            self.game_over_changed.emit(self._is_game_over)
            self.current_reaction_limit = self.base_reaction_limit
            self.start_time = time.time()
            
            self.universal_timer.start()
            self._spawn_next_red()

    def _spawn_next_red(self):
        if self._is_game_over:
            return
        # 9x9 grid equals indices 0 to 80
        new_index = random.randint(0, 80)
        # Ensure it does not spawn in the exact same spot twice in a row
        while new_index == self._red_index:
            new_index = random.randint(0, 80)
            
        self._red_index = new_index
        self.red_index_changed.emit(self._red_index)

        # Start/Reset internal reaction timer with scaled interval speed
        self.reaction_timer.stop()
        self.reaction_timer.setInterval(int(self.current_reaction_limit))
        self.reaction_timer.start()

    def _update_universal_clock(self):
        elapsed = time.time() - self.start_time
        self._universal_time_str = f"{elapsed:.1f}s"
        self.universal_time_changed.emit(self._universal_time_str)

    def _handle_time_up(self):
        # Triggered if user fails to click before internal countdown expires
        self._trigger_game_over()

    def _trigger_game_over(self):
        self.universal_timer.stop()
        self.reaction_timer.stop()
        elapsed_total = time.time() - self.start_time

        # Store top 3 scores
        if len(max_heap) < 3:
            heapq.heappush(max_heap, elapsed_total)
        else:
            if elapsed_total > max_heap[0]:
                heapq.heapreplace(max_heap, elapsed_total)

        self.top_scores_changed.emit()
        self._final_time_str = f"{elapsed_total:.2f} seconds"
        self.final_time_changed.emit(self._final_time_str)
        
        self._red_index = -1
        self.red_index_changed.emit(self._red_index)
        
        self._is_game_over = True
        self.game_over_changed.emit(self._is_game_over)

    # Process square coordinates grid input from user clicks
    @pyqtProperty(int)
    def handle_click(self):
        return -1

    @handle_click.setter
    def handle_click(self, index):
        if self._is_game_over or self._red_index == -1:
            return

        if index == self._red_index:
            # Correct Click: Scale down limit duration (increase difficulty by 10%)
            self.current_reaction_limit = max(self.minimum_reaction_limit, self.current_reaction_limit * 0.90)
            self._spawn_next_red()
        else:
            # Wrong Click: Game over instantly
            self._trigger_game_over()
