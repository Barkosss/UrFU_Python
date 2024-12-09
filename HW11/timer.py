import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Timer")

        buttonStartTimer = QPushButton("Start")

        self.setCentralWidget(buttonStartTimer)

    def click_button(self):
        print("Clicked!")



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()