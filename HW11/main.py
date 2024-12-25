import datetime
import sys

from PyQt6.QtCore import Qt, QDateTime, QTimer, QUrl
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtWidgets import (QApplication, QPushButton, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QMainWindow, QDateTimeEdit, QFileDialog, QSpinBox)


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        # Окно
        self.setWindowTitle("Stopwatch")
        self.setMinimumWidth(400)
        self.setMaximumWidth(400)
        #self.setFixedSize(600, 400)

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
        times_layout = QHBoxLayout()
        action_layout = QHBoxLayout()
        time_layout = QHBoxLayout()
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Время и текст
        self.time_label = QLabel("0 Seconds", self)
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_label.setStyleSheet("font-size: 32px;")

        self.date_time = QDateTimeEdit(datetime.datetime.now())
        self.date_time.setDisplayFormat("dd-MM-yyyy HH:mm:ss")
        self.date_time.setStyleSheet("""
            QDateTimeEdit {
                font-size: 24px;           /* Крупный текст */
                color: white;             /* Белый текст */
                background-color: black;  /* Чёрный фон */
                border: 2px solid white;  /* Белая рамка */
                border-radius: 8px;       /* Скруглённые углы */
                padding: 10px;            /* Внутренний отступ */
            }
            QDateTimeEdit::up-button, QDateTimeEdit::down-button {
                width: 30px;              /* Ширина кнопок */
                background-color: white;  /* Белый фон кнопок */
                border: none;             /* Убираем рамку */
                color: black
            }
            QDateTimeEdit::up-arrow {
                width: 20px;              /* Размер стрелки */
                height: 20px;
                color: black;
                content: "^"; /* Задайте путь к иконке или используйте стандартную */
            }
            QDateTimeEdit::down-arrow {
                width: 20px;              /* Размер стрелки */
                height: 20px;
                color: black;
                content: "v"; /* Задайте путь к иконке или используйте стандартную */
            }
            QDateTimeEdit::up-button:hover, QDateTimeEdit::down-button:hover {
                background-color: lightgray; /* Цвет кнопки при наведении */
            }
            QDateTimeEdit::drop-down {
                border-left: 1px solid white; /* Разделительная линия между кнопками */
            }
        """)
        self.date_time.setFixedHeight(60)  # Высота поля
        self.date_time.setMinimumWidth(300)  # Минимальная ширина поля

        layout.addWidget(self.time_label)
        layout.addWidget(self.date_time)

        # Поля ввода
        self.year_box = QSpinBox(self)  # Год
        self.year_box.setRange(datetime.datetime.now().year, 3000)
        self.year_box.setValue(datetime.datetime.now().year)
        times_layout.addWidget(self.year_box)

        self.month_box = QSpinBox(self)  # Месяц
        self.month_box.setRange(0, 12)
        self.month_box.setValue(0)
        times_layout.addWidget(self.month_box)

        self.week_box = QSpinBox(self)  # Неделя
        self.week_box.setRange(0, 4)
        self.week_box.setValue(0)
        times_layout.addWidget(self.week_box)

        self.day_box = QSpinBox(self)  # Дни
        self.day_box.setRange(0, 31)
        self.day_box.setValue(0)
        times_layout.addWidget(self.day_box)

        self.hour_box = QSpinBox(self)  # Часы
        self.hour_box.setRange(0, 24)
        self.hour_box.setValue(0)
        times_layout.addWidget(self.hour_box)

        self.minute_box = QSpinBox(self)  # Минуты
        self.minute_box.setRange(0, 60)
        self.minute_box.setValue(0)
        times_layout.addWidget(self.minute_box)

        self.second_box = QSpinBox(self)  # Секунды
        self.second_box.setRange(0, 60)
        self.second_box.setValue(0)
        times_layout.addWidget(self.second_box)

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

        self.button_notify_remove = QPushButton("🔕", self)
        self.button_notify_remove.setStyleSheet(
            "QPushButton { background-color: #822525; }"
        )
        self.button_notify_remove.clicked.connect(self.button_notify_delete)
        self.button_notify_remove.setFixedSize(50, 50)
        self.button_notify_remove.setVisible(False)

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
        action_layout.addWidget(self.button_notify_remove)
        action_layout.addWidget(self.button_start)
        action_layout.addWidget(self.button_pause)
        action_layout.addWidget(self.button_reset)

        time_layout.addWidget(self.button_start_one_minutes)
        time_layout.addWidget(self.button_start_five_minutes)
        time_layout.addWidget(self.button_start_fifteen_minutes)

        layout.addLayout(times_layout)
        layout.addLayout(action_layout)
        layout.addLayout(time_layout)
        central_widget.setLayout(layout)

    def update_timer(self):
        """Обновление времени"""
        try:
            formatter_time = self.format_time(self.time_clock)

            # Динамическое изменение размера окна
            if formatter_time.count("\n") >= 4:
                self.setMaximumHeight(500)
                self.resize(400, 1000)
            else:
                self.setMaximumWidth(400)
                self.resize(400, 400)

            if self.time_clock >= 0:
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
                ("Years", 31556952),
                ("Months", 2629746),
                ("Weeks", 604800),
                ("Days", 86400),
                ("Hours", 3600),
                ("Minutes", 60),
                ("Seconds", 1),
            ]

            result = []
            for name, unit_seconds in units:
                time = seconds // unit_seconds
                if time:
                    result.append(f"{name}: {time}")
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
            file_path, _ = QFileDialog.getOpenFileName(self, "Выберите аудиофайл", "",
                                                       "Audio Files (*.mp3 *.wav *.ogg)")
            if file_path:
                file_url = QUrl.fromLocalFile(file_path)
                self.media_player.setSource(file_url)
                self.button_notify.setStyleSheet("QPushButton {background-color: #2191FB;}")
                self.button_notify_remove.setVisible(True)

        except Exception as err:
            print(f"ERROR | Notify load: {err}")

    def button_notify_delete(self):
        try:
            self.button_notify_remove.setVisible(False)
            self.button_notify.setStyleSheet("QPushButton {background-color: #3c3c3c;}")
            self.media_player = QMediaPlayer()
            self.audio_output = QAudioOutput()
            self.media_player.setAudioOutput(self.audio_output)

        except Exception as err:
            print(f"ERROR | Notify remove: {err}")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
