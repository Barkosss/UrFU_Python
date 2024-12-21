import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QLabel, QMainWindow


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("stopwatch & Clock")
        self.setGeometry(300, 300, 300, 300)
        self.time = 60

        # Создаем компоновку для кнопок
        layout = QVBoxLayout()

        # Создаем виджет центрального окна
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Метка для отображения времени
        self.time_label = QLabel("Timer", self)
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_label.setStyleSheet("font-size: 32px;")
        layout.addWidget(self.time_label)

        # Создаем кнопки
        self.start_timer = QPushButton("Start")
        self.start_timer.clicked.connect(self.start_timer)
        self.start_timer.setFixedSize(100, 50)

        self.pause_timer = QPushButton("Pause")
        self.pause_timer.clicked.connect(self.start_timer)
        self.pause_timer.setFixedSize(100, 50)

        # Добавляем кнопки в компоновку
        layout.addWidget(self.start_timer)
        layout.addWidget(self.pause_timer)

        # Устанавливаем компоновку на центральный виджет
        central_widget.setLayout(layout)

    def start_timer(self):
        """Начать отсчёт таймера"""
        pass

    def pause_timer(self):
        """Поставить отсчёт таймера на паузу"""
        pass


app = QApplication(sys.argv)
self = MainWindow()
self.show()
app.exec()
