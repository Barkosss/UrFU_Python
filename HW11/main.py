import datetime
import sys

from PyQt6.QtCore import Qt, QDateTime, QTimer, QUrl, QSize
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtWidgets import (QApplication, QPushButton, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QMainWindow, QDateTimeEdit, QFileDialog)

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        # Окно
        self.setWindowTitle("Stopwatch")
        self.setMinimumHeight(400)
        self.setMaximumHeight(500)
        self.setMinimumWidth(400)
        self.setMaximumWidth(400)

        # Поля
        self.time_clock = 60
        self.is_running = False
        self.is_pause = False
        self.error_label = None

        # Таймер
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)

        # Аудио
        self.media_player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.media_player.setAudioOutput(self.audio_output)
        self.button_notify = QPushButton("🔔")
        self.button_notify.setFixedSize(50, 50)
        self.button_notify.clicked.connect(self.button_notify_load)

        # Виджеты
        layout = QVBoxLayout()
        action_layout = QHBoxLayout()
        time_layout = QHBoxLayout()
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Время и текст
        self.time_label = QLabel("0 Seconds", self)
        self.date_time = QDateTimeEdit(datetime.datetime.now())
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_label.setStyleSheet("font-size: 32px;")
        layout.addWidget(self.time_label)
        layout.addWidget(self.date_time)

        # Кнопки
        self.button_start = QPushButton("Start")  # Начать таймер
        self.button_start.setStyleSheet(
            "QPushButton { font-size: 24px; font-weight: 700; height: 50px; width: 150px;"
            "background-color: #70C17F; color: white; }"
            "QPushButton:hover { background-color: #B3D8BA; }"
            "QPushButton:pressed { background-color: #DF5349; }"
        )
        self.button_start.clicked.connect(self.button_start_timer)
        self.button_start.setFixedSize(100, 50)

        self.button_pause = QPushButton("Pause")  # Остановить таймер
        self.button_pause.setStyleSheet(
            "QPushButton { font-size: 24px; font-weight: 700; height: 50px; width: 150px;"
            "background-color: #F0B67F; color: white; }"
            "QPushButton:hover { background-color: #D6A271; }"
            "QPushButton:pressed { background-color: #DF5349; }"
        )
        self.button_pause.clicked.connect(self.button_pause_timer)
        self.button_pause.setFixedSize(100, 50)

        self.button_reset = QPushButton("Reset")  # Обнулить таймер
        self.button_reset.setStyleSheet(
            "QPushButton {"
            "font-size: 24px; font-weight: 700;height: 50px; width: 150px;"
            "background-color: #FE5F55; color: white; }"
            "QPushButton:hover { background-color: #DF5349; }"
            "QPushButton:pressed { background-color: #DF5349; }"
        )
        self.button_reset.clicked.connect(self.button_reset_timer)
        self.button_reset.setFixedSize(100, 50)

        # Предзаписанные кнопки
        self.button_start_one_minutes = QPushButton("1 Minutes")
        self.button_start_one_minutes.clicked.connect(lambda: self.button_start_timer(1))
        self.button_start_one_minutes.setFixedSize(100, 50)

        self.button_start_five_minutes = QPushButton("5 Minutes")
        self.button_start_five_minutes.clicked.connect(lambda: self.button_start_timer(5))
        self.button_start_five_minutes.setFixedSize(100, 50)

        self.button_start_fifteen_minutes = QPushButton("15 Minutes")
        self.button_start_fifteen_minutes.clicked.connect(lambda: self.button_start_timer(15))
        self.button_start_fifteen_minutes.setFixedSize(100, 50)

        action_layout.addWidget(self.button_notify)
        action_layout.addWidget(self.button_start)
        action_layout.addWidget(self.button_pause)
        action_layout.addWidget(self.button_reset)

        time_layout.addWidget(self.button_start_one_minutes)
        time_layout.addWidget(self.button_start_five_minutes)
        time_layout.addWidget(self.button_start_fifteen_minutes)

        layout.addLayout(action_layout)
        layout.addLayout(time_layout)
        central_widget.setLayout(layout)

    def update_timer(self):
        """Обновление времени"""
        try:
            formatter_time = self.format_time(self.time_clock)
            # TODO: Изменять размер
            if self.time_clock > 0:
                self.time_clock -= 1
                self.time_label.setText(formatter_time)
            else:
                self.timer.stop()
                self.is_running = False
                self.time_label.setText("Время вышло!")
                self.media_player.play()

        except Exception as err:
            print(f"ERROR | Update timer: {err}")

    @staticmethod
    def format_time(seconds: int) -> str:
        """Форматирование времени"""
        try:
            units = [
                ("years", 31556952),
                ("months", 2629746),
                ("weeks", 604800),
                ("days", 86400),
                ("hours", 3600),
                ("minutes", 60),
                ("seconds", 1),
            ]

            result = []
            for name, unit_seconds in units:
                time = seconds // unit_seconds
                if time:
                    result.append(f"{time} {name}")
                seconds %= unit_seconds

            return "\n".join(result)
        except Exception as err:
            print(f"ERROR | Format time: {err}")

    def button_start_timer(self, start_time: int = 0):
        """Запустить таймер"""
        try:
            self.media_player.stop()
            target_time = QDateTime().currentDateTime()

            if start_time and not self.is_pause:
                target_time = QDateTime.currentDateTime().addSecs(start_time * 60)
            elif not start_time and not self.is_pause:
                target_time = self.date_time.dateTime()

            # Если таймер был поставлен на паузу - Возобновить
            if self.is_pause:
                self.is_pause = False
                self.timer.start(1000)

            # Запустить таймер
            elif not self.is_running:
                current_time = QDateTime.currentDateTime()
                try:
                    if target_time > current_time:
                        # Время до выбранной даты
                        self.time_clock = current_time.secsTo(target_time)
                        self.is_running = True
                        # Таймер срабатывает каждую секунду
                        self.timer.start(1000)
                    else:
                        self.time_label.setText("Укажите будущее время")
                except Exception:
                    self.time_label.setText("Укажите будущее время")

        except Exception as err:
            print(f"ERROR | Start timer: {err}")

    def button_pause_timer(self):
        """Поставить таймер на паузу"""
        try:
            self.media_player.stop()
            self.timer.stop()
            self.is_pause = True
            self.is_running = False

        except Exception as err:
            print(f"ERROR | Pause timer: {err}")

    def button_reset_timer(self):
        """Сбросить таймер"""
        try:
            self.media_player.stop()
            self.timer.stop()
            self.is_running = False
            self.time_clock = 0
            self.time_label.setText("0 Seconds")
        except Exception as err:
            print(f"ERROR | Reset timer: {err}")

    def button_notify_load(self):
        """Установка звука для уведомления"""
        try:
            # Открыть диалог выбора файла
            # TODO: Менять иконку и добавить название аудио
            file_path, _ = QFileDialog.getOpenFileName(self, "Выберите аудиофайл", "",
                                                       "Audio Files (*.mp3 *.wav *.ogg)")
            if file_path:
                file_url = QUrl.fromLocalFile(file_path)
                self.media_player.setSource(file_url)

        except Exception as err:
            print(f"ERROR | Notify load: {err}")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
